def create_learning_outcomes_prompt(course_name, topic_name, session_name, reading_material):
    """
    Creates a structured prompt for generating learning outcomes based on the provided details.

    Args:
        course_name (str): Name of the course.
        topic_name (str): Name of the topic.
        session_name (str): Name of the session.
        reading_material (str): The reading material in markdown format.

    Returns:
        str: A formatted prompt for OpenAI to generate learning outcomes.
    """
    prompt = f"""
    You are an AI that helps create learning outcomes for educational content. 

    Given the following details, generate clear and concise learning outcomes for the session:

    Course Name: {course_name}
    Topic Name: {topic_name}
    Session Name: {session_name}
    
    I want you to act as an experienced content developer. How is expert in organising the content to improve the effective ness of learning.

Your task is to create possible learning outcomes based on the given session summary and reading material.

These learning outcomes will be tagged to coding practices and multiple choice questions to understand effectiveness of the session through data gathered from the users.

Given the learning outcomes as a list of strings:
All the string should be in snake case


## Session Summary and Reading Material:
```
Reading Material: {reading_material}
```
    The learning outcomes should be:
    - Measurable
    - Actionable
    - Aligned with the course objectives
    - Focused on key takeaways from the session
    
    Guidelines :-
    - All the Learning outcomes should be simple it should not contain Very long name its should be not have spaces it should only have underscore(_)
    - Result must be in a sequence of learning outcomes seperated by comma
    
    sample output:
    learningoutcome1,learningoutcome2,learningoutcome3
    """
    return prompt
