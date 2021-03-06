#: Title : Kaldi_text2variKN_corpus.py
#: Author : "Ahmed Ismail" <ahmed.ismail.zahran@gmail.com>
#: Version : 1.0
#: Description : Transform Kaldi text to variKN corpus
#    through removing utterance id and adding start and end tags
#: Arguments :
#  1- Path to kaldi text
#  2- Destination of variKN corpus

import argparse
import codecs

__author__ = "Ahmed Ismail"
__license__ = "GPL"
__version__ = "1.0"
__email__ = "ahmed.ismail.zahran@gmail.com"
__status__ = "Development"

def main():
    ''' Transforms Kaldi text file to corpus file ready for processing by variKN
    '''
    # Parse command line arguments
    arg_parser = argparse.ArgumentParser(description=('Transform Kaldi text'
        'file to coprus ready for processing by variKN.'))
    arg_parser.add_argument('kaldi_text', type=str,
        help=(('Path to the file'
            'containing the Kaldi text corpus.')))
    arg_parser.add_argument('output_corpus', type=str,
        help=(('Path to output'
            'file to save the corpus.')))
    args = vars(arg_parser.parse_args())

    text_file_path = args['kaldi_text']
    corpus_file_path = args['output_corpus']
    
    # Open the Kaldi text file and the output corpus as streams
    # (It may be infeasible to perform offline processing in case of large
    # Kaldi text files)
    kaldi_text_file = codecs.open(text_file_path, 'r', encoding='utf-8')
    corpus_file = codecs.open(corpus_file_path, 'w', encoding='utf-8')
    
    # For each line in the Kaldi text, remove the utterance-id and add
    # variKN sentence start and end symbols (<s> and </s> respectively)
    for line in kaldi_text_file:
        line = ' '.join(line.strip().split()[1:])
        line_varikn = '<s> ' + line + ' </s>\n'
        corpus_file.write(line_varikn)
    kaldi_text_file.close()
    corpus_file.close()


if __name__ == '__main__':
    main()
