from collections import Counter # For counting highest frequencies
bigram_counts = dict()
output = 'output.txt'
unique_bigrams = 0

# Read in the config file
with open(output) as file:
        # Split based on newlines
        output_lines = file.read().splitlines()
        for line in output_lines:
                # Parse the lines of the output by splitting by whitespace (spaces and tabs)
                line = line.split()
                # Set the bigram key to the first two words
                key = line[0] + ' ' + line[1]
                # Set the biram frequency value to the third word 
                value = int(line[2])
                bigram_counts[key] = value
                unique_bigrams += 1


# 1
print('Number of Unique Bigrams: {}\n'.format(unique_bigrams))

print('Examples of Unique Bigrams:\n')
list_of_bigrams = list(bigram_counts.items())
for i, (key, value) in enumerate(list_of_bigrams[:3], start=1):
    print('\t{:>2}) {:>16}  {:>4}'.format(i, key, value))
print('\n')


# 2
print('10 Most Frequent Bigrams and their Frequencies:\n')
# The Counter module provides the most_common() method to guage highest frequencies
bigram_counter = Counter(bigram_counts)
frequent_bigrams = bigram_counter.most_common(10)
for i, (key, value) in enumerate(frequent_bigrams, start=1):
    print('\t{:>2}) {:>16}  {:>4}'.format(i, key, value))
print('\n')


# 3
number_of_most_frequent_bigrams = 0
for (key, value) in frequent_bigrams:
    number_of_most_frequent_bigrams += value
print('Cumulative Frequency of 10 Most Frequent Bigrams: {}\n'.format(number_of_most_frequent_bigrams))

number_of_bigrams = sum(bigram_counter.values())
print('Cumulative Frequency of All Bigrams: {}\n'.format(number_of_bigrams))

fraction = number_of_most_frequent_bigrams/number_of_bigrams
print('Faction of 10 Most Frequent Bigrams to All Bigrams: {}/{} = {:.8f} = {:.6f}%\n'.format(number_of_most_frequent_bigrams, number_of_bigrams, fraction, fraction*100))


# 4
number_of_singly_occurring_bigrams = 0
singly_occurring_bigrams = list()
for (key, value) in list_of_bigrams:
    if value == 1:
        number_of_singly_occurring_bigrams += 1
        if len(singly_occurring_bigrams) < 3:
            singly_occurring_bigrams.append(key)
print('Number of Singly Occurring Bigrams: {}\n'.format(number_of_singly_occurring_bigrams))

print('Examples of Singly Occurring Bigrams:\n')
for i, key in enumerate(singly_occurring_bigrams, start=1):
    print('\t{:>2}) {:>16}'.format(i, key))
print('\n')


# 5
print('5 Most Frequent Words Following \"Light\" and their Frequencies\n')
# Loop through bigrams to find those that start with "light"
light_bigrams = dict()
for (key, value) in list_of_bigrams:
    words = key.split()
    if words[0] == 'light':
        light_bigrams[key] = value
# The Counter module provides the most_common() method to gauge highest frequencies
light_bigram_counter = Counter(light_bigrams)
frequent_light_bigrams = light_bigram_counter.most_common() # Note that all 7 words following "light" have count 1, so I didn't limit it to 5 bigrams
for i, (key, value) in enumerate(frequent_light_bigrams, start=1):
    print('\t{:>2}) {:>16}  {:>4}'.format(i, key, value))
print('\n')
