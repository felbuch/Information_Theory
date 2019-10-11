# Information_Theory
Some Python functions to calculate the main concepts in Information Theory

These functions were originally developed as part of a course I took at Duke University.

All functions require numpy to be imported with the alias np.
The log2 function file already imports numpy with this alias for you.

In addition, note that the functions of some files may depend on functions from other files.
For example, the KL function, which calculates the Kullback-Leibler divergence, uses the crossentropy and the entropy functions.

All functions bring a description of what they do and their parameters.
We also opt to use argument names which, as much as possible, are faithful to the object types of these arguments.
For example, list_of_probabilities is a list, and array_of_joint_probabilities is a numpy array.
