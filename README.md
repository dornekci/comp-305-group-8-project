# COMP 305 Spring 2021 Project: Neighbors of Our Kingdom


## Implemented by:
* Ahmet Kadir Zeybek 64509
* Doruk Örnekci      64570
* Ece Güz            69002
* Zeynep Sıla Kaya   69101

## To Do List:
* ~~Learn how to use Git/Github for the project.~~
* ~~Search for data structures and algorithms which can be used in the project.~~
* ~~Learn how to use Pandas library and its methods for file reading.~~
* ~~Search for an efficient graph library and tools for graph visualizaton.~~
* ~~Email to TA about the parts you did not understand.~~
* ~~Think about other algorithms other than Prim and Kruskal.~~
* ~~Visualiaze the given first test file.~~ 
* ~~Investigate if the problem is np.~~ 
* ~~Brute Force only solved the first test file, find a more effective solution.~~
* ~~Begin the presentation preparations.~~
* ~~A more efficient algorithm was found for the 2nd file, but it doesn't work for the 3rd file.~~
* Find a more efficient algorithm that can work in the third file.(Could not find)
 
## How to Run the Code:
* After user runs the program, they can decide on the existing algorithms. User selects between 3 test files and 3 existing algorithms by giving the corresponding number as an input. 


## Result of the Test Cases:
*1* Brute-force algorithm, for each node it searches for all neighbors to get the minimum distinct neighbors. Since it searches for all m-sized (desired kingdom size) combinations; it suffers from high complexity. Therefore, the program are only able to run test file 1.
*2* This algorithm searches for a city in a kingdom which will cause less distinct neighbors. When it starts from a city, it looks at the neighbors of the city and picks the one which will minimize the number of distinct neighbors. This algorithms works well on test file 1 and test file 2. Unfortunately, it still cannot run the million-citied test file 3.
*3* At first, the algorthims searchs for the cities with the less neighbors, then pair them. In the rest of the algorithm, similar algorithm in the 2nd one is used while examining these pairs. It works accurate on test file 1 but it finds non-minimum kingdom. When the pairing increases, the run time and the accuracy decreases. 


## Summary of the Final Algorithm:
* It decreases the run time significantly. However, the accuracy also decreased. Still, it cannot execute test file 3 in desirable time. 
