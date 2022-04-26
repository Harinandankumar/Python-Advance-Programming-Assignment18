#!/usr/bin/env python
# coding: utf-8

# 1. A robot has been given a list of movement instructions. Each instruction is
# either left, right, up or down, followed by a distance to move. The robot starts
# at [0, 0]. You want to calculate where the robot will end up and return its final
# position as a list.
# To illustrate, if the robot is given the following instructions:
# [&quot;right 10&quot;, &quot;up 50&quot;, &quot;left 30&quot;, &quot;down 10&quot;]
# It will end up 20 left and 40 up from where it started, so we return [-20, 40].
# Examples
# track_robot([&quot;right 10&quot;, &quot;up 50&quot;, &quot;left 30&quot;, &quot;down 10&quot;]) ➞ [-20, 40]
# track_robot([]) ➞ [0, 0]
# // If there are no instructions, the robot doesn&#39;t move.
# track_robot([&quot;right 100&quot;, &quot;right 100&quot;, &quot;up 500&quot;, &quot;up 10000&quot;]) ➞ [200, 10500]
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[1]:


def track_robot(in_list):
    output = [0,0]
    for ele in in_list:
        ele = ele.split(" ")
        if ele[0] in ['right','left']:
            output[0] = output[0]-int(ele[1]) if ele[0] == 'left' else output[0]+int(ele[1])
        else:
            output[1] = output[1]-int(ele[1]) if ele[0] == 'down' else output[1]+int(ele[1])
    print(f'track_robot({in_list}) ➞ {output}')
        
track_robot(["right 10", "up 50", "left 30", "down 10"])
track_robot([])
track_robot(["right 100", "right 100", "up 500", "up 10000"])


# 2. Write a function that will return the longest word in a sentence. In cases
# where more than one word is found, return the first one.
# Examples
# find_longest(&quot;A thing of beauty is a joy forever.&quot;) ➞ &quot;forever&quot;
# find_longest(&quot;Forgetfulness is by all means powerless!&quot;) ➞ &quot;forgetfulness&quot;
# find_longest(&quot;\&quot;Strengths\&quot; is the longest and most commonly used word that
# contains only a single vowel.&quot;) ➞ &quot;strengths&quot;
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[2]:


def find_longest(in_string):
    len_list = []
    for ele in in_string.split(' '):
        len_list.append(len(ele))
    print(f'find_longest({in_string}) ➞ {in_string.split(" ")[len_list.index(max(len_list))].lower()}')
        
find_longest("A thing of beauty is a joy forever.")
find_longest("Forgetfulness is by all means powerless!")
find_longest("\"Strengths\" is the longest and most commonly used word that contains only a single vowel.")


# 3. Create a function to check if a candidate is qualified in an imaginary coding
# interview of an imaginary tech startup.
# The criteria for a candidate to be qualified in the coding interview is:
# 1. The candidate should have complete all the questions.
# 2. The maximum time given to complete the interview is 120 minutes.
# 3. The maximum time given for very easy questions is 5 minutes each.
# 4. The maximum time given for easy questions is 10 minutes each.
# 5. The maximum time given for medium questions is 15 minutes each.
# 6. The maximum time given for hard questions is 20 minutes each.
# 
# If all the above conditions are satisfied, return &quot;qualified&quot;, else return
# &quot;disqualified&quot;.
# You will be given a list of time taken by a candidate to solve a particular
# question and the total time taken by the candidate to complete the interview.
# Given a list , in a true condition will always be in the format [very easy, very
# easy, easy, easy, medium, medium, hard, hard].
# The maximum time to complete the interview includes a buffer time of 20
# minutes.
# Examples
# interview([5, 5, 10, 10, 15, 15, 20, 20], 120) ➞ &quot;qualified&quot;
# interview([2, 3, 8, 6, 5, 12, 10, 18], 64) ➞ &quot;qualified&quot;
# interview([5, 5, 10, 10, 25, 15, 20, 20], 120) ➞ &quot;disqualified&quot;
# # Exceeded the time limit for a medium question.
# interview([5, 5, 10, 10, 15, 15, 20], 120) ➞ &quot;disqualified&quot;
# # Did not complete all the questions.
# interview([5, 5, 10, 10, 15, 15, 20, 20], 130) ➞ &quot;disqualified&quot;
# # Solved all the questions in their respected time limits but exceeded the total
# time limit of the interview.
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[3]:


def interview(in_list, in_time):
    output = 'qualified'
    if in_time > 120 or max(in_list[0:2]) > 5 or max(in_list[2:4]) > 10 or max(in_list[4:6]) > 15 or max(in_list[6:8]) > 20 or len(in_list) != 8:
            output = 'disqualified'
    print(f'interview{in_list,in_time} ➞ {output}')
    
interview([5, 5, 10, 10, 15, 15, 20, 20], 120)
interview([2, 3, 8, 6, 5, 12, 10, 18], 64)
interview([5, 5, 10, 10, 25, 15, 20, 20], 120)
interview([5, 5, 10, 10, 15, 15, 20], 120)
interview([5, 5, 10, 10, 15, 15, 20, 20], 130)


# 
# 4. Write a function that divides a list into chunks of size n, where n is the
# length of each chunk.
# Examples
# chunkify([2, 3, 4, 5], 2) ➞ [[2, 3], [4, 5]]
# chunkify([2, 3, 4, 5, 6], 2) ➞ [[2, 3], [4, 5], [6]]
# chunkify([2, 3, 4, 5, 6, 7], 3) ➞ [[2, 3, 4], [5, 6, 7]]
# chunkify([2, 3, 4, 5, 6, 7], 1) ➞ [[2], [3], [4], [5], [6], [7]]
# chunkify([2, 3, 4, 5, 6, 7], 7) ➞ [[2, 3, 4, 5, 6, 7]]
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[4]:


def chunkify(in_list,chunk_size):
    output = []
    for i in range(0,len(in_list),chunk_size):
        output.append(in_list[i:i+chunk_size])
    print(f'chunkify{in_list, chunk_size} ➞ {output}')
    
chunkify([2, 3, 4, 5], 2)   
chunkify([2, 3, 4, 5, 6], 2)
chunkify([2, 3, 4, 5, 6, 7], 3)
chunkify([2, 3, 4, 5, 6, 7], 1)
chunkify([2, 3, 4, 5, 6, 7], 7)


# 5. You are given a list of strings consisting of grocery items, with prices in
# parentheses. Return a list of prices in float format.
# 
# Examples
# get_prices([&quot;salad ($4.99)&quot;]) ➞ [4.99]
# get_prices([
# &quot;artichokes ($1.99)&quot;,
# &quot;rotiserrie chicken ($5.99)&quot;,
# &quot;gum ($0.75)&quot;
# ])
# ➞ [1.99, 5.99, 0.75]
# get_prices([
# &quot;ice cream ($5.99)&quot;,
# &quot;banana ($0.20)&quot;,
# &quot;sandwich ($8.50)&quot;,
# &quot;soup ($1.99)&quot;
# ])
# ➞ [5.99, 0.2, 8.50, 1.99]
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[5]:


def get_prices(in_list):
    out_list = []
    for ele in in_list:
        out_list.append(float((ele.split('$')[-1]).split(')')[0]))
    print(f'get_prices({in_list}) ➞ {out_list}')
        
get_prices(["salad ($4.99)"])
get_prices(["artichokes ($1.99)","rotiserrie chicken ($5.99)","gum ($0.75)"])
get_prices(["ice cream ($5.99)","banana ($0.20)","sandwich ($8.50)","soup ($1.99)"])

