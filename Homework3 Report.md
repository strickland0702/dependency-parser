# SI630 Homework 3 Report

## Task 2

For each epoch, we draw the accuracy versus iteration plot and loss versus iteration plot. And then at last, we concatenate the loss curve and accuracy curve of those five epochs in a single plot for clearness.  

#### Epoch 1

![image-20210403223447574](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20210403223447574.png)

![image-20210403223555461](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20210403223555461.png)

#### Epoch 2

![image-20210403225313500](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20210403225313500.png)

![image-20210403225331915](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20210403225331915.png)

#### Epoch 3

![image-20210403225356292](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20210403225356292.png)

![image-20210403225734420](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20210403225734420.png)

#### Epoch 4

![image-20210403225742596](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20210403225742596.png)

![image-20210403225818002](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20210403225818002.png)

#### Epoch 5

![image-20210403225855647](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20210403225855647.png)

![image-20210403225911530](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20210403225911530.png)

#### Total Accuracy and Loss (5 epochs concatenated)

![image-20210403230257324](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20210403230257324.png)

![image-20210403230324078](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20210403230324078.png)

#### UAS Score 

![image-20210331185441747](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20210331185441747.png)

In this plot, the model was trained for three times to show variance of the UAS Score on test data. The UAS Score result is shown in the table below.

|         | Experiment 1 | Experiment 2 | Experiment 3 |
| ------- | ------------ | ------------ | ------------ |
| Epoch 1 | 76.89        | 76.26        | 76.67        |
| Epoch 2 | 81.16        | 80.48        | 80.92        |
| Epoch 3 | 83.16        | 82.34        | 83.13        |
| Epoch 4 | 84.07        | 83.88        | 83.89        |
| Epoch 5 | 84.80        | 83.91        | 84.79        |

***Findings***

From the loss and accuracy plot for each epoch, we can see the accuracy curve climbed fast and loss curve also declined fast at epoch 1. For epoch 2 and 3, the speed of accuracy climbing and loss declining slowed down, but the tendency still remained. From epoch 4 the accuracy stopped climbing and the loss stopped decreasing, both the plots fluctuate in a random way. So 3 epochs training should be appropriate for this model.

## Task 3

In my new parser model TwoHiddenParserModel, I tried different network designs and hyperparameters. The model is different from the original model in: 

- There are 2 hidden layers with l1_hidden_size = 500 and l2_hidden_size = 200.

- The activation function is changed from cube to ReLU.

- The l1_hidden_size was changed from 200 to 500.

  ![image-20210331193329879](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20210331193329879.png)

Then we measure the test UAS score of these two models for each training epoch. The result of a model with single hidden layer but using ReLU activation function is also shown for reference. 

|      | Single Hidden Layer + Cube (Old) | Single Hidden Layers + ReLU (Reference) | Two Hidden Layers + ReLU (New) |
| :--: | :------------------------------: | :-------------------------------------: | :----------------------------: |
|  1   |              76.89               |                  82.33                  |             82.48              |
|  2   |              81.86               |                  85.48                  |             86.48              |
|  3   |              83.16               |                  86.51                  |             87.34              |
|  4   |              84.07               |                  87.57                  |             87.82              |
|  5   |              84.80               |                  88.00                  |             88.48              |

From the result above we can see, the change of activation function from cube to ReLU improved the UAS Score a lot. The change from one hidden layer to two hidden layers further improved the performance a bit further.

## Task 4

The output of parsing sentence "The big dog ate my homework" was shown below. The parser made some mistakes when parsing the first half of the sentence.

```
----
buffer: ['the', 'big', 'dog', 'ate', 'my', 'homework']
stack:  ['<root>']
action: shift
----
buffer: ['big', 'dog', 'ate', 'my', 'homework']
stack:  ['<root>', 'the']
action: shift
----
buffer: ['dog', 'ate', 'my', 'homework']
stack:  ['<root>', 'the', 'big']
action: shift
----
buffer: ['ate', 'my', 'homework']
stack:  ['<root>', 'the', 'big', 'dog']
action: shift
----
buffer: ['my', 'homework']
stack:  ['<root>', 'the', 'big', 'dog', 'ate']
action: left arc, <d>:compound
----
buffer: ['my', 'homework']
stack:  ['<root>', 'the', 'big', 'ate']
action: left arc, <d>:amod
----
buffer: ['my', 'homework']
stack:  ['<root>', 'the', 'ate']
action: left arc, <d>:det
----
buffer: ['my', 'homework']
stack:  ['<root>', 'ate']
action: shift
----
buffer: ['homework']
stack:  ['<root>', 'ate', 'my']
action: shift
----
buffer: []
stack:  ['<root>', 'ate', 'my', 'homework']
action: left arc, <d>:nmod:poss
----
buffer: []
stack:  ['<root>', 'ate', 'homework']
action: right arc, <d>:dep
----
buffer: []
stack:  ['<root>', 'ate']
action: right arc, <d>:root
    <root>
      |
     ate
  ____|___________
 |    |     |  homework
 |    |     |     |
the  big   dog    my
```

The correct operation for each step should be: 

```
----
buffer: ['the', 'big', 'dog', 'ate', 'my', 'homework']
stack:  ['<root>']
action: shift
----
buffer: ['big', 'dog', 'ate', 'my', 'homework']
stack:  ['<root>', 'the']
action: shift
----
buffer: ['dog', 'ate', 'my', 'homework']
stack:  ['<root>', 'the', 'big']
action: shift
----
buffer: ['ate', 'my', 'homework']
stack:  ['<root>', 'the', 'big', 'dog']
action: left arc
----
buffer: ['ate', 'my', 'homework']
stack:  ['<root>', 'the', 'dog']
action: left arc,
----
buffer: ['ate', 'my', 'homework']
stack:  ['<root>', 'dog']
action: shift,
----
buffer: ['my', 'homework']
stack:  ['<root>', 'dog', 'ate']
action: left arc, 
----
buffer: ['my', 'homework']
stack:  ['<root>', 'ate']
action: shift
----
buffer: ['homework']
stack:  ['<root>', 'ate', 'my']
action: shift
----
buffer: []
stack:  ['<root>', 'ate', 'my', 'homework']
action: left arc, 
----
buffer: []
stack:  ['<root>', 'ate', 'homework']
action: right arc,
----
buffer: []
stack:  ['<root>', 'ate']
action: right arc,    
```

