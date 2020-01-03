#!/bin/bash
test_var_path='../../vars/temp/main.yml'
var_files=(
"../../vars/php.yml"
)
var_files_one=(
"../../vars/temp/empty.yml"
)
length="${#var_files[@]}"
for ((i=0;i<$length;i++)); do 
    > $test_var_path
    cat ${var_files[i]} > $test_var_path
    echo -e "\n" >> $test_var_path
    cat "${var_files_one[i]}" | grep -v "^---" >> $test_var_path
    echo -e "content in test_var_path >> \n\n`cat $test_var_path`\n\n"
    molecule test
    > $test_var_path
done

echo "${#var_files[@]}"