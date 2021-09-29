import numpy as np

import matplotlib.pyplot as plt

sampleNo = 1;
mu = 85;
sigma = 0.4

for i in range(10):
	s = np.random.normal(mu, sigma, sampleNo)
	print(s)

plt.plot(s,'o-')
plt.show()

print(""