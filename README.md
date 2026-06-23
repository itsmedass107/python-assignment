# Prompt Library for Content Generation

**Name:** T Nikhil Dass
**Course:** Generative AI 

---

# Prompt 1 – Social Media Post (LinkedIn)


Create a LinkedIn post for a hackathon achievement.


* Role Prompting
* Constraints


You are a LinkedIn branding expert.

Write a LinkedIn post about my participation in {hackathon_name}.

Achievement:
{achievement}

Constraints:

* Under 150 words
* Professional tone
* End with gratitude

## Sample Output

🚀 Excited to share my experience participating in Hackxelerate'26!

Working alongside my team, we developed a Women Safety Platform designed to provide emergency support and safe-route assistance.

The event challenged us to think creatively, collaborate effectively, and build real-world solutions.

Grateful to my teammates, mentors, and organizers for this opportunity.

#Hackathon #Innovation #Technology

---

# Prompt 2 – Blog Post Intro Paragraph


Generate a blog introduction.


* Role Prompting
* Context


You are an expert blogger.

Write a blog introduction on:

Topic: {topic}

Length: 100 words.

## Sample Output

Artificial Intelligence is transforming education by making learning more personalized and efficient. From intelligent tutoring systems to automated assessments, AI is helping students learn faster and educators teach more effectively.

---

# Prompt 3 – Cold Outreach Email


Offer website development services.


* Role Prompting
* Constraints


You are a sales professional.

Write a cold email to {business_name}.

Service:
{service}

Keep it under 120 words.

## Sample Output

Subject: Website Development Services

Hello,

I came across your business and was impressed by your work. I specialize in developing modern websites that help businesses improve their online presence and customer engagement.

I would love to discuss how I can help your business.

Thank you.

---

# Prompt 4 – Follow-Up Email


Follow up after a previous email.

* Context Prompting
* Professional Tone


Write a follow-up email to {client_name}.

Previous discussion:
{discussion}

Tone: Professional

## Sample Output

Subject: Follow-Up

Hello Sir,

I hope you are doing well.

I wanted to follow up regarding my previous email about website development services. Please let me know if you would like to discuss further.

Thank you.

---

# Prompt 5 – Product Description


Describe Smart Campus Voting System.

* Persona Prompting
* Constraints

You are a product marketing expert.

Write a product description for:

Product:
{product_name}

Features:
{features}

Maximum 100 words.

## Sample Output

Smart Campus Voting System is a secure digital platform that enables students to vote safely and efficiently. It features OTP verification, campus authentication, and an intuitive dashboard for administrators.

---

# Prompt 6 – YouTube Title + Description


Generate educational content.


* Role Prompting
* SEO Optimization


You are a YouTube SEO expert.

Generate:

1. Title
2. Description

Topic:
{topic}

## Sample Output

Title:
Python for Beginners | Learn Python in 20 Minutes

Description:
Master Python fundamentals with this beginner-friendly tutorial covering variables, loops, and functions.

---

# Prompt 7 – Newsletter Section


Monthly Tech Club Update.


* Structured Output
* Context Prompting


You are a newsletter editor.

Create a newsletter section for:

Event:
{event}

Format:
Headline
Summary

## Sample Output

Headline:
Tech Club Monthly Highlights

Summary:
This month, students participated in coding competitions, attended AI workshops, and collaborated on innovative projects.

---

# Prompt 8 – Article Summarization


Summarize AI articles.

* Constraints
* Structured Output


Summarize the following article:

{article_text}

Output:

* Key Points
* Conclusion

Maximum 150 words.

## Sample Output

Key Points:

* AI improves productivity.
* AI supports automation.
* AI enhances decision-making.

Conclusion:
AI is becoming a key technology across industries.

---

# Prompt 9 – FAQ Generator


Women Safety Platform FAQs.


* Structured Output
* Role Prompting


You are a customer support specialist.

Generate 5 FAQs for:

Product:
{product_name}

Format:
Question
Answer

## Sample Output

Q1: What is the Women Safety Platform?
A: It is a safety-focused platform providing emergency support.

Q2: Does it support live location tracking?
A: Yes.

Q3: Can emergency contacts be added?
A: Yes.

---

# Prompt 10 – 7-Day Content Calendar


PosterHaus Promotion.


* Role Prompting
* Structured Output


You are a content strategist.

Create a 7-day content calendar for:

Business:
{business_name}

Format:
Day
Topic
Caption Idea

## Sample Output

Day 1 – Introduction to PosterHaus

Day 2 – Featured Car Posters

Day 3 – Customer Reviews

Day 4 – Greek God Collection

Day 5 – Behind the Scenes

Day 6 – Limited Time Offers

Day 7 – Call to Action

---

# Iteration Example 1

## V1

Write a LinkedIn post about my hackathon.

## Problem

Too generic.

## V2

You are a LinkedIn branding expert.

Write a LinkedIn post about my participation in Hackxelerate'26.

Achievement:
Women Safety Platform

Constraints:

* Professional tone
* Under 150 words

## Improvement

More specific and produces better output.

---

# Iteration Example 2

## V1

Write a product description.

## Problem

Lacks details.

## V2

Write a product description for Smart Campus Voting System.

Features:
OTP verification, secure login, admin dashboard.

## Improvement

More informative and relevant.

---

# Iteration Example 3

## V1

Summarize this article.

## Problem

Output may be inconsistent.

## V2

Summarize this article.

Output:

* Key Points
* Conclusion

Maximum 150 words.

## Improvement

Produces structured and concise summaries.
