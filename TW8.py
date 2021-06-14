import numpy as np


# %%
import pandas as pd
emails = pd.read_csv('./emails.csv')


# %%
emails[:10]


# %%
def process_email(text):
    text = text.lower()
    return list(set(text.split()))

emails['words'] = emails['text'].apply(process_email)


# %%
emails[:10]


# %%
num_emails = len(emails)
num_spam = sum(emails['spam'])

print("Number of emails:", num_emails)
print("Number of spam emails:", num_spam)
print()

# Calculating the prior probability that an email is spam
print("Probability of spam:", num_spam/num_emails)

# %% [markdown]
# ### 2. Training a naive Bayes model
# 
# Our plan is to write a dictionary, and in this dictionary record every word, and its pair of occurrences in spam and ham

# %%
model = {}

# Training process
for index, email in emails.iterrows():
    for word in email['words']:
        if word not in model:
            model[word] = {'spam': 1, 'ham': 1}
        if word in model:
            if email['spam']:
                model[word]['spam'] += 1
            else:
                model[word]['ham'] += 1


# %%
model['lottery']


# %%
model['sale']

# %% [markdown]
# ### 3. Using the model to make predictions

# %%
def predict_bayes(word):
    word = word.lower()
    num_spam_with_word = model[word]['spam']
    num_ham_with_word = model[word]['ham']
    return 1.0*num_spam_with_word/(num_spam_with_word + num_ham_with_word)


# %%
predict_bayes('lottery')


# %%
predict_bayes('sale')


# %%
def predict_naive_bayes(email):
    total = len(emails)
    num_spam = sum(emails['spam'])
    num_ham = total - num_spam
    email = email.lower()
    words = set(email.split())
    spams = [1.0]
    hams = [1.0]
    for word in words:
        if word in model:
            spams.append(model[word]['spam']/num_spam*total)
            hams.append(model[word]['ham']/num_ham*total)
    prod_spams = np.long(np.prod(spams)*num_spam)
    prod_hams = np.long(np.prod(hams)*num_ham)
    return prod_spams/(prod_spams + prod_hams)


# %%
predict_naive_bayes('lottery sale')


# %%
predict_naive_bayes('Hi mom how are you')


# %%
predict_naive_bayes('Hi MOM how aRe yoU afdjsaklfsdhgjasdhfjklsd')


# %%
predict_naive_bayes('meet me at the lobby of the hotel at nine am')


# %%
predict_naive_bayes('enter the lottery to win three million dollars')


# %%
predict_naive_bayes('buy cheap lottery easy money now')


# %%
predict_naive_bayes('Grokking Machine Learning by Luis Serrano')


# %%
predict_naive_bayes('asdfgh')


# %%
