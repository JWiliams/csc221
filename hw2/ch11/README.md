Activity 1
In this activity they wanted me to redirect outputs from commands that I came up with into other files.

Activity 2
In this activity, I was challenged to see if I can list only the 20th last file in the directory/etc.
I list the etc/ directory and numbered its lines. I also sent the output of that numbered list to my temp
directory and named it list.
From there I made this command: " cut -f 17 -d ' ' list | nl | uniq | sed -n '9,10p;11q' "
The output was the 20th file in the etc/ directory.

Activity 3
In this exercise, I had to go to my home directory and see how many files I had executable permission for. 
I long listed the directory and made a file out of it and moved the file to my temp file. There I only focused on
line that had 'rwx' characters in it and that was beside each other.
I used this command: " egrep '[rwx]{3,}' homeD | wc -l "
I can execute 37 files in my home directory.



