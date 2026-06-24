# MINI PROJECT: Prompt Library for Content Generation

**Name:** T Nikhil Dass  
**Department:** B.Tech Information Technology  
**Year:** First Year  
**Course:** Generative AI

---

## Prompt 1: LinkedIn Post for Product Launch

### Use Case
Create a LinkedIn post announcing a product launch.

### Techniques Used
- Role Prompting
- Few-shot Prompting
- Constraints

### Template

```text
You are a senior LinkedIn content writer.

Write a LinkedIn post announcing the launch of {product_name}.

Product Description: {product_description}

Target Audience: {audience}

Example 1:
"We are happy to introduce our new product. It helps users save time and improve productivity."

Example 2:
"Our latest product is designed to make daily tasks easier and faster."

Constraints:
- Maximum 120 words
- Use simple language
- Include 2 emojis
- End with a question
```

### Sample Output

**Input**

```text
product_name = SmartNote
product_description = AI note-taking application
audience = College students
```

**Output**

```text
We are happy to introduce SmartNote!
SmartNote is an AI-powered note-taking application designed for college students. It helps organize notes, create summaries, and improve productivity.
Whether preparing for exams or managing projects, SmartNote can make studying easier.
Have you ever wished your notes could organize themselves?
```

### Iteration

**V1 Prompt**

```text
Write a LinkedIn post about SmartNote.
```

**Problem:** Too generic.

**V2 Prompt**

Added role, examples, audience and constraints.

**Improvement:** More professional and targeted output.

---

## Prompt 2: YouTube Title + Description Generator

### Use Case
Generate YouTube titles and descriptions.

### Techniques Used
- Role Prompting
- Placeholders
- Constraints

### Template

```text
You are a YouTube content creator.

Create a title and description for a video.

Topic: {topic}

Audience: {audience}

Constraints:
- Title under 60 characters
- Description under 100 words
- Use keywords naturally
```

### Sample Output

**Input**

```text
topic = Python Basics for Beginners
audience = First-Year Engineering Students
```

**Output**

```text
Title:
Python Basics for Beginners | Complete Starter Guide

Description:
Learn Python programming from scratch. This video covers variables, loops, and functions in an easy way. Perfect for engineering students starting their coding journey.
```

### Iteration

**V1 Prompt**

```text
Generate a YouTube title.
```

**Problem:** Lacks context.

**V2 Prompt**

Added topic, audience and constraints.

**Improvement:** More relevant and useful output.

---

## Conclusion

This mini project demonstrates:

- Role Prompting
- Few-shot Prompting
- Constraints
- Placeholders
- Prompt Iteration

These techniques help generate more accurate and reusable AI responses.
