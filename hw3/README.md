***********************************Part 1
        To begin, I ran the program lab_setup.py in the hw3 directory. 
    It created a part1 and part2 folder. In the part1 folder nearly 200 hundred files are
    filled with text and the first part of the assignment was to see which of these 200
    hundred files has the word "achar" in them.
    In the achar directory, which is a folder I created in the part1 directory, using the command: mkdir achar, I typed
    "egrep -R 'achar' ../". The command egrep searches for the string of characters 'achar' in 
    the parent folder. So basically it serched for 'achar' in the part1 folder, but more specificaly, it
    searched for 'achar' in the 200 hundred files. 'achar' was found in these 20 files:
    ../file00001:achar
    ../file00011:achar
    ../file00021:achar
    ../file00031:achar
    ../file00041:achar
    ../file00051:achar
    ../file00061:achar
    ../file00071:achar
    ../file00081:achar
    ../file00091:achar
    ../file00101:achar
    ../file00111:achar
    ../file00121:achar
    ../file00131:achar
    ../file00141:achar
    ../file00151:achar
    ../file00161:achar
    ../file00171:achar
    ../file00181:achar
    ../file00191:achar  
    Now, at this part of the assignment, I am to move the files found into the the achar folder found in the part1 directory, but before I did that I notice something special about the files. The file numbers ended in 1, which is great. I now have a clear way to move the files. I type the command 
    "cp *1 achar" which copied the 20 files found to the achar folder. '*1' is a 
    wildcard that is targeting any fileneames that ends in 1.

    I did the same steps for the next word 'adducts'. I type this command in the part1 directory:
    egrep -R 'adducts' and it found these files:
    ./file00005:adducts
    ./file00015:adducts
    ./file00025:adducts
    ./file00035:adducts
    ./file00045:adducts
    ./file00055:adducts
    ./file00065:adducts
    ./file00075:adducts
    ./file00085:adducts
    ./file00095:adducts
    ./file00105:adducts
    ./file00115:adducts
    ./file00125:adducts
    ./file00135:adducts
    ./file00145:adducts
    ./file00155:adducts
    ./file00165:adducts
    ./file00175:adducts
    ./file00185:adducts
    ./file00195:adducts
    These files end with the number 5. So, I typed this command: "cp *5 adducts/". 
    This copied the files to the adducts directory.

    Next word was 'aquaregia'. To search the files in the part1 directory I typed:
    "egrep -R 'aquaregia' ..". 
    It found:
    ./file00002:aquaregia
    ./file00012:aquaregia
    ./file00022:aquaregia
    ./file00032:aquaregia
    ./file00042:aquaregia
    ./file00052:aquaregia
    ./file00062:aquaregia
    ./file00072:aquaregia
    ./file00082:aquaregia
    ./file00092:aquaregia
    ./file00102:aquaregia
    ./file00112:aquaregia
    ./file00122:aquaregia
    ./file00132:aquaregia
    ./file00142:aquaregia
    ./file00152:aquaregia
    ./file00162:aquaregia
    ./file00172:aquaregia
    ./file00182:aquaregia
    ./file00192:aquaregia
    These files end in 2. So I typed this command: "cp *2 aquaregia/". The 20 files ending in the number 2 were copied and moved to the aquaregia file.

    The third word is 'daystars' and by typing the command: "egrep -R 'daystars' .."
    I found 20 files that was in the parent directory of the folder I was currently in. (The '..' was used because I was in the 'daystars' directory and needed to search files in the 'part1' directory that is also the parent of 'daystars'.)
    ../file00008:daystars
    ../file00018:daystars
    ../file00028:daystars
    ../file00038:daystars
    ../file00048:daystars
    ../file00058:daystars
    ../file00068:daystars
    ../file00078:daystars
    ../file00088:daystars
    ../file00098:daystars
    ../file00108:daystars
    ../file00118:daystars
    ../file00128:daystars
    ../file00138:daystars
    ../file00148:daystars
    ../file00158:daystars
    ../file00168:daystars
    ../file00178:daystars
    ../file00188:daystars
    ../file00198:daystars
    These 20 files were copied and moved to the file named 'daystars' using the command: "cp *8 daystars/".

    The fourth word is identificational. I did what I did before and typed the 
    command: "egrep -R 'identificational' .." after I made a directory named 'identificational'. All the results ended with 9.
    ../file00009:identificational
    ../file00019:identificational
    ../file00029:identificational
    ../file00039:identificational
    ../file00049:identificational
    ../file00059:identificational
    ../file00069:identificational
    ../file00079:identificational
    ../file00089:identificational
    ../file00099:identificational
    ../file00109:identificational
    ../file00119:identificational
    ../file00129:identificational
    ../file00139:identificational
    ../file00149:identificational
    ../file00159:identificational
    ../file00169:identificational
    ../file00179:identificational
    ../file00189:identificational
    ../file00199:identificational
    I copied these files to the directory 'identificational'
    command: "cp *9 identificational/"

    The fifth word was meiosis. It was in these following files.
    (command: egrep -R 'meiosis' ..)
    ../part1/file00000:meiosis
    ../part1/file00010:meiosis
    ../part1/file00020:meiosis
    ../part1/file00030:meiosis
    ../part1/file00040:meiosis
    ../part1/file00050:meiosis
    ../part1/file00060:meiosis
    ../part1/file00070:meiosis
    ../part1/file00080:meiosis
    ../part1/file00090:meiosis
    ../part1/file00100:meiosis
    ../part1/file00110:meiosis
    ../part1/file00120:meiosis
    ../part1/file00130:meiosis
    ../part1/file00140:meiosis
    ../part1/file00150:meiosis
    ../part1/file00160:meiosis
    ../part1/file00170:meiosis
    ../part1/file00180:meiosis
    ../part1/file00190:meiosis
    Copied to the meiosis directory. The command I used was "cp *0 meiosis/"

    The sixth word was overaggressively. It was in these following files.
    (command: egrep -R 'overaggressively' ..)
    ../file00006:overaggressively
    ../file00016:overaggressively
    ../file00026:overaggressively
    ../file00036:overaggressively
    ../file00046:overaggressively
    ../file00056:overaggressively
    ../file00066:overaggressively
    ../file00076:overaggressively
    ../file00086:overaggressively
    ../file00096:overaggressively
    ../file00106:overaggressively
    ../file00116:overaggressively
    ../file00126:overaggressively
    ../file00136:overaggressively
    ../file00146:overaggressively
    ../file00156:overaggressively
    ../file00166:overaggressively
    ../file00176:overaggressively
    ../file00186:overaggressively
    ../file00196:overaggressively
    Copied to the overaggressively directory. The command I used was "cp *6 overaggressively/"

    The seventh word was pyrheliometer. It was in these following files.
    (command: egrep -R 'pyrheliometer' ..)
    ../file00004:pyrheliometer
    ../file00014:pyrheliometer
    ../file00024:pyrheliometer
    ../file00034:pyrheliometer
    ../file00044:pyrheliometer
    ../file00054:pyrheliometer
    ../file00064:pyrheliometer
    ../file00074:pyrheliometer
    ../file00084:pyrheliometer
    ../file00094:pyrheliometer
    ../file00104:pyrheliometer
    ../file00114:pyrheliometer
    ../file00124:pyrheliometer
    ../file00134:pyrheliometer
    ../file00144:pyrheliometer
    ../file00154:pyrheliometer
    ../file00164:pyrheliometer
    ../file00174:pyrheliometer
    ../file00184:pyrheliometer
    ../file00194:pyrheliometer
    Copied to the pyrheliometer directory. The command I used was "cp *4 pyrheliometer/"

    The eigth word was scattered. It was in these following files.
    (command: egrep -R 'scattered' ..)
    ../file00003:scattered
    ../file00013:scattered
    ../file00023:scattered
    ../file00033:scattered
    ../file00043:scattered
    ../file00053:scattered
    ../file00063:scattered
    ../file00073:scattered
    ../file00083:scattered
    ../file00093:scattered
    ../file00103:scattered
    ../file00113:scattered
    ../file00123:scattered
    ../file00133:scattered
    ../file00143:scattered
    ../file00153:scattered
    ../file00163:scattered
    ../file00173:scattered
    ../file00183:scattered
    ../file00193:scattered
    Copied to the scattered directory. The command I used was "cp *3 scattered/".

    The final word was wheeldom. It was in these following files.
    (command: egrep -R 'wheeldom' ..)
    ../file00007:wheeldom
    ../file00017:wheeldom
    ../file00027:wheeldom
    ../file00037:wheeldom
    ../file00047:wheeldom
    ../file00057:wheeldom
    ../file00067:wheeldom
    ../file00077:wheeldom
    ../file00087:wheeldom
    ../file00097:wheeldom
    ../file00107:wheeldom
    ../file00117:wheeldom
    ../file00127:wheeldom
    ../file00137:wheeldom
    ../file00147:wheeldom
    ../file00157:wheeldom
    ../file00167:wheeldom
    ../file00177:wheeldom
    ../file00187:wheeldom
    ../file00197:wheeldom
    Copied to the wheeldom directory. The command I used was "cp *7 wheeldom/".

    Part 2

    For this part, I was to go to the part 2 directory. My command was "cd courses/csc221/hw3/part2". My first task was to sort the shuffled-words.txt directory. My command that I typed was: "sort shuffled-words.txt > shuffled-words-sorted.txt". I added the '>' because I wanted the result to be a file in the part2 directory named 'shuffled-words-sorted.txt'.
    My output of the command: "cat shuffled-words-sorted.txt"

    abbotcy
    abdominoscopy
    abducting
    abecedarium
    accidentiality
    accurate
    achar
    achar
    achoke
    achoke
    acronichal
    acronichal
    acronichal
    acrosomes
    acyetic
    adatis
    adaunt
    adducible
    adducible
    adducible
    adducible
    adducible
    adducible
    adducible
    adducts ...

    The next excercise was to find 10 of the most common words in the file rand-words.txt. So I type the command: "sort shuffled-words.txt | uniq -c | sort -nr | head -10 > common-words.txt". I first sorted it because I wanted my next command to perfrom in a certain way. Uniq -c tells us how many of a certain word there are, but it only does it sequentially. If it sees cat on the first line, dog on the next, and cat again on the final line, it would output “1 cat, 1 dog, 1 cat”. However if it is done sequentially, cat, cat, dog. Then the output would be “2 cat, 1 dog”. Which is why Uniq -c was the second command called. Sort -nr is listing the words in order of the most used word to the least. Head -10 list the first 10 words of the list, specifically most 10 common words in this command. The >, like in the first excercise, moved the results of the commands into a file that was created and named 'common-words.txt' in the part2 directory.
    My output:  43 persuasory
                30 venography
                28 anaplasia
                25 unprejudicated
                21 botulismus
                20 mattaro
                19 underaccident
                19 feston
                16 systematizing
                16 meteors

    The third part was to do the exact same thing we did in the last excercise on a file name rand-numbers.txt. Since I'm working with the rand-numbers.txt file my command this time was "sort rand-numbers.txt | uniq -c | sort -nr | head -10 > common-numbers.txt". It created a file named common-numbers.txt that has the results in it. 
    My output:  40 34478
                17 60805
                15 87439
                13 20727
                9 90408
                8 96400
                8 9077
                8 63261
                7 65275
                6 98081

    In the fourth excercise I was to produce a list of the 10 most common number pairs. My command was: "sort rand-numbers-2.txt | uniq -c | sort -nr | head -10 > common-2.txt".
    My output:  47 83979   92646
                27 15065   76014
                15 40972   21633
                13 91103   5194
                12 46369   45065
                11 52871   41714
                10 99625   32867
                10 61095   25257
                 9 85566   37402
                 8 87255   76502    

    In the final excercise I was to produce a list of the 10 most common number triples out of five columns in the rand-number-5.txt. I did seven commands. One for each column subselections.
    1,2,3 - "cut -c -21 rand-numbers-5.txt | sort | uniq -c | sort -nr | head -10 > 123.txt"
    2,3,4 - "cut -c 9-29 rand-numbers-5.txt | sort | uniq -c | sort -nr | head -10 > 234.txt"
    3,4,5 - "cut -c 17- rand-numbers-5.txt | sort | uniq -c | sort -nr | head -10 > 345.txt"
    1,3,4 - "cut -c -8,17-29 rand-numbers-5.txt | sort | uniq -c | sort -nr | head -10 > 134.txt"
    1,4,5 - "cut -c -8,25- rand-numbers-5.txt | sort | uniq -c | sort -nr | head -10 > 145.txt"
    1,3,5 - "cut -c -8,17-24,33- rand-numbers-5.txt | sort | uniq -c | sort -nr | head -10 > 135.txt"
    2,4,5 - "cut -c 9-16,25- rand-numbers-5.txt | sort | uniq -c | sort -nr | head -10 > 245.txt"
    To breakdown the commands, the first part of the command was cut. Cut -c (range) <filename> is responsible for selecting characters by their position. Sort, just like the previous exercises, was used to get the number triples in order and was used before uniq to make uniq work a certain way. Uniq -c is used to count duplications. Sort -nr sorts the triples by the number of how many times it was duplicated and list the results from greatest to least. Head -10 shows the first 10 lines. Finally the > <filename>, was used because I wanted to seperate the results into their respected files. I did this because I wanted all the results to be in one file. So I made the common-5.txt in visual studio and copy and paste my results from the column.txt files into common-5.txt
