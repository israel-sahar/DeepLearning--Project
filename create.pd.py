import pandas as pd
import os
from pydub import AudioSegment
import math
import subprocess
from shutil import copyfile

from pydub.utils import make_chunks

ffmpeg = "/usr/local/bin/ffmpeg"

PATH = 'all-samples/all-samples/'
FULL_PATH = 'F:/New folder/study-2021/DeepLearning/project/all-samples/all-samples/'
FOLDERS_NAMES = ['cello', 'clarinet', 'flute', 'guitar', 'oboe', 'saxophone', 'trumpet', 'viola','piano','drum']

def create_table():
    data = []
    for folder in FOLDERS_NAMES:
        for file in sorted(os.listdir(PATH + folder)):
            data.append((file, folder, 1))

    df = pd.DataFrame(data, columns=['fname', 'label', 'manually_verified'])
    df.to_csv('train.csv')

def convert_mp3_to_wav():
    # convert wav to mp3
    for folder in ['piano']:
        for file in sorted(os.listdir(FULL_PATH + folder)):
            try:
                if file.endswith('.mp3'):
                    name_file = file.replace('.mp3', '')
                    src = FULL_PATH + folder + '/' + file
                    sound = AudioSegment.from_mp3(src)
                    sound.export(FULL_PATH + folder + '/' + name_file + '.wav', format="wav")
                    os.remove(FULL_PATH + folder + '/' + file)
            except:
                os.remove(FULL_PATH + folder + '/' + file)
                continue

DRUM_PATH = 'F:/New folder/study-2021/DeepLearning/project/freesound-audio-tagging/'
NEW_DRUM_PATH = PATH + 'drum/'
TEST_CSV_PATH=DRUM_PATH+'test_post_competition.csv'
TRAIN_CSV_PATH=DRUM_PATH+'train_post_competition.csv'

TEST = 'audio_test/'
TRAIN= 'audio_train/'

def pullDrumAudios():
    df= pd.read_csv(TEST_CSV_PATH)
    df = df[df['label'].str.contains('drum')]
    for fname in df['fname']:
        file_path = DRUM_PATH+TEST+fname
        new_path  = FULL_PATH + 'drum/drum_' + fname
        copyfile(file_path, new_path)

    df= pd.read_csv(TRAIN_CSV_PATH)
    df = df[df['label'].str.contains('drum')]
    for fname in df['fname']:
        file_path = DRUM_PATH+TRAIN+fname
        new_path  = FULL_PATH + 'drum/drum_' + fname
        copyfile(file_path, new_path)

FILE_FOR_TEST_PATH = 'F:/New folder/study-2021/DeepLearning/project/Brahms I Gestillte Sehnsucht, Op. 91 for Viola, Clarinet and Piano_160k.mp3'
#sound = AudioSegment.from_mp3(FILE_FOR_TEST_PATH)
#sound.export(FILE_FOR_TEST_PATH.replace('mp3','') + '.wav', format="wav")

#sound = AudioSegment.from_wav(FILE_FOR_TEST_PATH.replace('mp3','') + '.wav')
#chunk_length_ms = 60000 # pydub calculates in millisec
#chunks = make_chunks(sound, chunk_length_ms)
#for i, chunk in enumerate(chunks):
#    chunk_name = "chunk{0}.wav".format(i)
#    chunk.export(chunk_name, format="wav")


def create_table_for_test():
    data = []
    PATH ='F:/New folder/study-2021/DeepLearning/project/test02/'
    for file in sorted(os.listdir(PATH)):
        data.append((file))

    df = pd.DataFrame(data, columns=['fname'])
    df.to_csv('testing02.csv')

create_table_for_test()

def splittest():
    PATH = 'F:/New folder/study-2021/DeepLearning/project/piano/wav/test2.wav'
    sound = AudioSegment.from_wav('F:/New folder/study-2021/DeepLearning/project/piano/wav/test2.wav')
    chunk_length_ms = 1000 # pydub calculates in millisec
    chunks = make_chunks(sound, chunk_length_ms)
    for i, chunk in enumerate(chunks):
        chunk_name = "chunk_1_"+"{0}".format(i).zfill(3)+".wav"
        chunk.export('F:/New folder/study-2021/DeepLearning/project/test02/'+chunk_name, format="wav")

#splittest()