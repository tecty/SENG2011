#!/bin/bash
function gen_list()
{
    for (( i = 1; i < 5; i++ )); do
      # grep the priority by order
      egrep "\[$i\]" project_requirement_list.txt |
        sed "s/\[$i\]//g" |
        sed "s/^/\- \[ \] \[$i\]/g" |
        sed "s/^$//g" |
        sed "s/$/  /g"
    done
}

gen_list
