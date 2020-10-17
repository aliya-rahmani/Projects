read -p "Enter Word :" Word
read -p "Enter Character To Check Occurence In Word :" char
echo "$Word" | tr -cd "$char" | wc -c
