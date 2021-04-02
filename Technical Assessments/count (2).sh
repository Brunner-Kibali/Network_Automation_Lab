# separate the lines and store them in an array called 'lines'
IFS=$'\n' read -d '' -r -a lines < /var/log/access.log

# 'ip_addresses is an associative array. Stores key pair values. Will tell us how many times each ip address has been found
# {
#        '111.222.333.124': 13,
#         '10.0.0.1': 20,
#         '1.1.1.1': 1
#              
#} 
declare -A ip_addresses

# make a dictionary of all tables
# {
#        '01/Feb/1998': 10,
#        '01/Mar/1998': 11
# }
declare -A dates



# lines = ['line1', 'line2']

# loop through the lines
for i in "${lines[@]}"
do
        counter=0

        # for each line we separate the words by tabs
        for x in `echo ${i%\t}`
        do
                counter=$((counter+1))

                # We look for the first word on the line [which is usually the IP address]
                if (( $counter == 1))
                then
                        # we check if the IP address already exists on the associative array ip_addresses
                        # if it does exist, we increase its counter by one
                        # if not, we intialize it to one
                        if ! [[ -v "ip_addresses[$x]" ]]; then
                                # initialize to the dict
                                ip_addresses[$x]=1
                        else
                                # add plus one
                                ip_addresses[$x]=$((ip_addresses[$x]+1))
                        fi
                elif (( $counter == 4 )); then
                        # x = [01/Feb/1998:01:08:39
                        # 01/Feb/1998

                        x="${x:1}"
                        # x = 01/Feb/1998:01:08:39
                        
                        IFS=: read -r d h m s <<< "$x"
                        # d = 01/Feb/1998
                        # h = 01
                        # m = 08
                        # s = 39

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