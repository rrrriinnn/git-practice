import numpy as np
import matplotlib.pyplot as plt

wt = np.random.uniform(40.0, 90.0, 100)
ht = np.random.randint(140, 200, 100)

bmi = (wt / (ht*0.01) ** 2)

Underweight = np.sum(bmi < 18.5)
Healthy = np.sum((bmi >= 18.5) & (bmi <= 24.9))
Overweight = np.sum((bmi >= 25.0) & (bmi <= 29.9)) 
Obese = np.sum(bmi >= 30.0)

counts = [Underweight, Healthy, Overweight, Obese]
labels = ["Underweight", "Healthy", "Overweight", "Obese"]

plt.bar(labels, counts)
plt.ylabel("Students")
plt.show()

plt.hist(bmi, bins = 6)
plt.xlabel("BMI")
plt.ylabel("Students")
plt.show()

plt.pie(counts, labels = labels, autopct = '%1.2f%%')
plt.show()

plt.scatter(ht, wt)
plt.xlabel("heights")
plt.ylabel("weights")
plt.show()