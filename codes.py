import csv
import math
import matplotlib.pyplot as plt

# Read the CSV file and extract the data
filename = 'your_file_name.csv'
data = []
with open(filename, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the first row
    for row in csv_reader:
        data.append(float(row[5]))

# Calculate the mean
mean = sum(data) / len(data)

# Calculate the median
sorted_data = sorted(data)
n = len(sorted_data)
if n % 2 == 0:
    median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
else:
    median = sorted_data[n//2]

# Calculate the variance
variance = sum((x - mean) ** 2 for x in data) / len(data)

# Calculate the standard deviation
standard_deviation = math.sqrt(variance)

# Calculate the standard error
standard_error = standard_deviation / math.sqrt(len(data))

n = len(data)
skewness = (sum((x - mean) ** 3 for x in data) / (n * standard_deviation ** 3))

if skewness < -0.5:
    distribution_shape = "Left-skewed"
elif skewness < 0.5:
    distribution_shape = "Symmetrical (Approximately normal)"
else:
    distribution_shape = "Right-skewed"

# Create an empty dictionary to store value-frequency pairs
frequency_dict = {}

# Count the frequency of each value in the data
for value in data:
    if value in frequency_dict:
        frequency_dict[value] += 1
    else:
        frequency_dict[value] = 1

# Find the maximum frequency
max_frequency = max(frequency_dict.values())

# Find the values with the maximum frequency (modes)
modes = [value for value, frequency in frequency_dict.items() if frequency == max_frequency]

if len(modes) == 1:
    print("The mode is:", modes[0])
else:
    print("The data has multiple modes:", modes)

# Find outliers
q1 = sorted_data[int(n * 0.25)]  # 1st quartile
q3 = sorted_data[int(n * 0.75)]  # 3rd quartile
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers = [x for x in data if x < lower_bound or x > upper_bound]

# Plot the histogram
plt.style.use('seaborn-v0_8-pastel')
plt.hist(data, bins=15, facecolor = '#2ab0ff', edgecolor='#169acf', linewidth=0.5)
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram of Data')
plt.show()

# Plot the boxplot
plt.boxplot(data)
plt.ylabel('Values')
plt.title('Boxplot of Data')
plt.show()

# Calculate the confidence interval for the mean
z_value = 1.96  # For a 95% confidence level
margin_of_error_mean = z_value * standard_error
lower_bound_mean = mean - margin_of_error_mean
upper_bound_mean = mean + margin_of_error_mean

# Calculate the confidence interval for the variance
z_value = 1.96  # For a 95% confidence level
margin_of_error_variance = z_value * math.sqrt(2 * variance**2 / (len(data) - 1))
lower_bound_variance = variance - margin_of_error_variance
upper_bound_variance = variance + margin_of_error_variance

# Calculate the required sample size
z_value = 1.645  # For a 90% confidence level (z-value from standard normal distribution)
required_sample_size = (z_value * standard_deviation / 0.1) ** 2
sample_size = math.ceil(required_sample_size)

print("Mean:", mean)
print("Median:", median)
print("Variance:", variance)
print("Standard Deviation:", standard_deviation)
print("Standard Error:", standard_error)
print("Outliers:", outliers)
print("Confidence Interval for Mean: ({}, {})".format(lower_bound_mean, upper_bound_mean))
print("Confidence Interval for Variance: ({}, {})".format(lower_bound_variance, upper_bound_variance))
print("Required sample size:", sample_size)
print("Distribution Shape:", distribution_shape)