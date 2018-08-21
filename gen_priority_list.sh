#!/bin/bash
function gen_list()
{
    # grep the priority by order 
    egrep "\[1\]" project_requirement_list.txt
    egrep "\[2\]" project_requirement_list.txt
    egrep "\[3\]" project_requirement_list.txt
    egrep "\[4\]" project_requirement_list.txt
}

gen_list 