# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "no"
    answers["(b)"] = "no"
    answers["(c)"] = "yes"
    answers["(d)"] = "yes"

    # explain-string: explanation in english prose
    answers["(a) explain"] = "A record satisfying both Home Owner is yes and Annual Income = Low is also yes, so two separate rules can be applicable for a single record. Thus not exclusive"
    answers["(b) explain"] = "It is not exhaustive, since the given rules doesnt account for Marital Status = Divorced"
    answers["(c) explain"] = "Since there are overlapping rules, ordering is necessary, also in general ordering the rules is a good practice. For example a record having both Home Owner = No and Marital Status = Single will satisfy two rules in the given rule set"
    answers["(d) explain"] = "We need default class because, when a record containing Marital Status = Divorced and Home Owner = No, it doesnt satisfy any of the given rules."

    return answers


# -----------------------------------------------------------
"""
def question2():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = None
    answers["(b)"] = None
    answers["(c)"] = None
    answers["(d)"] = None

    # explain_string: explanation in english prose
    answers["(a) explain"] = None
    answers["(b) explain"] = None
    answers["(c) explain"] = None
    answers["(d) explain"] = None

    return answers
"""
# -----------------------------------------------------------
def question3():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "yes"
    answers["(b)"] = "no"
    answers["(c)"] = "no"

    # explain-string: explanation in english prose
    answers["(a) example"] = "Based on the given rules and dataset, no vertebrate would be eligible to be classified as more than one class. Thus the rules are mutually exclusive."
    answers["(b) example"] = "Amphibians are not classified by any of these rules, thus these rules are not exhaustive"
    answers["(c) example"] = "There are no overlaps thus ordering not necessary"

    return answers
# -----------------------------------------------------------
def question7():
    answers = {}

    # bool: True/False
    answers["(a)"] = True
    answers["(b)"] = True
    answers["(c)"] = False
    answers["(d)"] = False

    # explain_string: explanation in english prose
    answers["(a) explain"] = "Gradient of weights are calculated using chain-rule. Thus the (k+1)th gradient can be calculated using the kth weight's gradient in back propagation since it goes from op layer to ip layer"
    answers["(b) explain"] = "The activation in the node of k+1 layer is weighted sum of the kth layer, thus can be used for the calculation."
    answers["(c) explain"] = "The given fact is called overfitting and not vanishing gradient"
    answers["(d) explain"] = "The gradient of loss would be 0 if the input is 0 or the loss is converged to global minimum"

    return answers

# -----------------------------------------------------------
def question8():
    answers = {}

    # float
    answers["(a) P(X_1=1)"] = 0.65
    answers["(a) P(X_2=1)"] = 0.41
    answers["(a) P(X_1=1,X_2=1)"] = 0.28

    # string: "dependent" or "independent"
    answers["(a) Relationship between X_1 and X_2"] = "dependent"

    # string: "yes" or "no"
    answers["(b) X_1 and X_2 conditionally independent given the class?"] = "yes"

    # float
    answers["(c) P(X_1=1 | +)"] = 0.8
    answers["(c) P(X_1=1 | -)"] = 0.5
    answers["(c) P(X_2=1 | +)"] = 0.5
    answers["(c) P(X_2=1 | -)"] = 0.32
    answers["(c) P(X_3=1 | +)"] = 0.4
    answers["(c) P(X_3=1 | -)"] = 0.16

    # For each row give the class predicted by the model after training using Naive Bayes
    # String: either '+' or '-'
    answers["(d) Row 1"] = '+'
    answers["(d) Row 2"] = '-'
    answers["(d) Row 3"] = '-'
    answers["(d) Row 4"] = '-'

    # float between 0 and 1
    answers["(d) Training error rate"] = None

    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = 5
    answers["(b) K"] = 5

    # explain_string
    answers["(a) explain"] = "Provides balance for k=5, since k=1 cosniders every point as one cluster and k=50 diluting the local structure of the data."
    answers["(b) explain"] = "It considers a small enough number of neighbors to capture the local patterns in the data, but not so less that it becomes overly sensitive to noise."

    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # float
    answers["(a) P(A=1|+)"] = 0.6
    answers["(a) P(B=1|+)"] = 0.4
    answers["(a) P(C=1|+)"] = 0.8
    answers["(a) P(A=1|-)"] = 0.4
    answers["(a) P(B=1|-)"] = 0.4
    answers["(a) P(C=1|-)"] = 0.2

    # type: explanatory string
    answers["(a) P(A=1|+) explain your answer"] = "Instances where class = + and A = 1 is 3 and Total instances where class = + is 5 thus 3/5 = 0.6"
  
    # type: float
    # note: R is the sample (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = 1.0
    answers["(b) P(R|+)"] = 0.2
    answers["(b) P(R|-)"] = 0.0  ## Verify

    # string, '+' or '-'
    answers["(b) class label"] = '+'

    # explain_string
    answers["(b) Explain your reasoning"] = "Naive Bayes for + class is 0.192 (multiply part a values where class is +) and - class is 0.032 thus + class is predicted using Naive Bayes"
  
    # float
    answers["(c) P(A=1)"] = 0.5
    answers["(c) P(B=1)"] = 0.4
    answers["(c) P(A=1,B=1)"] = 0.2

    # type: string, 'yes' or 'no'
    answers["(c) A independent of B?"] = 'yes'
  
    # type: float
    answers["(d) P(A=1)"] = 0.5
    answers["(d) P(B=0)"] = 0.6
    answers["(d) P(A=1,B=0)"] = 0.3

    # type: string: 'yes' or 'no'
    answers["(d) A independent of B?"] = 'yes'
  
    # type: float
    answers["(e) P(A=1,B=1|+)"] = 0.2
    answers["(e) P(A=1|+)"] = 0.6
    answers["(e) P(B=1|+)"] = 0.4

    # type: string: 'yes' or 'no'
    answers["(e) A independent of B given class +?"] = 'no'

    # type: explanatory string
    answers["(e) A and B conditionally independent given class +, explain"] =  "No since P(X|YZ)[0.5] != P(X|Z)[0.6], where X = (A=1), Y = (B=1) and Z = +"
  
    return answers
# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
