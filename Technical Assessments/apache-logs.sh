#!/usr/bin/env bash
# separate the lines and store them in an array called
# 'lines'
LOG_FILE="$1"

IFS=$'\n' read -d '' -r -a lines < "$LOG_FILE"

# 'ip_addresses is an associative array. Stores key pair values.
# Will tell us how many times each ip address has been found
declare -A ip_addresses

# make a dictionary of all tables
declare -A dates

# loop through the lines
for i in "${lines[@]}"
do
        counter=0

        # for each line we separate the words by tabs
        for x in `echo ${i%\t}`
        do
                counter=$((counter+1))

                # We look for the first word on the line
                # [which is usually the IP address]
                if (( $counter == 1))
                then
                        # we check if the IP address already exists
                        # on the associative array ip_addresses
                        # if it does exist, we increase its counter by
                        # one, if not, we intialize it to one
                        if ! [[ -v "ip_addresses[$x]" ]]; then
                                ip_addresses[$x]=1
                        else
                                ip_addresses[$x]=$((ip_addresses[$x]+1))
                        fi
                elif (( $counter == 4 )); then
                        x="${x:1}"
                        IFS=: read -r d h m s <<< "$x"
                        if ! [[ -v "dates[$d]" ]]; then
                                dates[$d]=1
                        else
                                dates[$d]=$((dates[$d]+1))
                        fi
                fi
        done
done

echo "-----DATES-----"
for i in "${!dates[@]}"
do
        echo "${dates[$i]}      $i"
done

echo "-----IP ADDRESS------"
for i in "${!ip_addresses[@]}"
do
        echo "${ip_addresses[$i]}       $i"
done
