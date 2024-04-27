## open file with numbers and show this most numbers

def main():
    with open('pbnumbers.txt', 'r') as file:
        data = file.read()
    numbers = [int(num) for num in data.split()]
    #print(numbers)
    ##create dictionary with count number of digits
    number_counts = create_dictionary_with_counter(numbers)
    #print(number_counts)     
    ##frequency of occurrence of numbers 
    counter_numbers = 0
    powerball_numbers = []
    other_numbers = []
    for num in numbers:
        counter_numbers += 1
        if counter_numbers / 6 == 1:
            powerball_numbers.append(num)
            counter_numbers = 0
        else:
            other_numbers.append(num)
    ##...other numbers
    frequency_other_numbers = create_dictionary_with_counter(other_numbers) 
    ##...powerball numbers
    frequency_powerball_numbers = create_dictionary_with_counter(powerball_numbers) 
    #print(frequency_powerball_numbers)
    #print(frequency_other_numbers)
    ##create dict with all most numbers (6 items)
    most_all_numbers = create_dictionary_with_most_numbers(number_counts)
    print('Most all numbers(number / number of repetitions):\n', most_all_numbers)   
    ##create dict with other most numbers (6 items)
    most_other_numbers = create_dictionary_with_most_numbers(frequency_other_numbers)
    print('Most other numbers(number / number of repetitions):\n', most_other_numbers)
    ##create dict with powerball most numbers (6 items)
    most_powerball_numbers = create_dictionary_with_most_numbers(frequency_powerball_numbers)
    print('Most powerball numbers(number / number of repetitions):\n', most_powerball_numbers)   
         
def create_dictionary_with_counter(list_numbers):
    dict_num_counts = {}
    for num in list_numbers:
        dict_num_counts[num] = dict_num_counts.get(num, 0) + 1
    return dict_num_counts

def create_dictionary_with_most_numbers(count):
    dict_numbers = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))
    tuples_numbers = list(dict_numbers.items())
    tuples_numbers = tuples_numbers[:6]
    most_numbers = {key: value for key, value in tuples_numbers}
    return most_numbers

main()



