# PawPal+ Project Reflection

## 1. System Design
**a. Initial design**
- Briefly describe your initial UML design.
My initial UML design maps out the four core components required for PawPal+: Owner, Pet, Task, and Scheduler. It shows a clear hierarchy where an Owner is linked to their Pet, while the central Scheduler gathers those pets and their specific Tasks to generate an organized daily plan.

- What classes did you include, and what responsibilities did you assign to each?
I included Owner (to store user details and link to their pets), Pet (to hold specific animal data like species and name), and Task (to track care activities, durations, and priorities). Finally, the Scheduler class acts as the system's brain, responsible for collecting the tasks and executing the logic to organize them into a final schedule.


**b. Design changes**
- Did your design change during implementation?

- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs
**a. Constraints and priorities**
- What constraints does your scheduler consider (for example: time, priority, preferences)?

- How did you decide which constraints mattered most?


**b. Tradeoffs**
- Describe one tradeoff your scheduler makes.

- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration
**a. How you used AI**
- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?

- What kinds of prompts or questions were most helpful?


**b. Judgment and verification**
- Describe one moment where you did not accept an AI suggestion as-is.

- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification
**a. What you tested**
- What behaviors did you test?

- Why were these tests important?


**b. Confidence**
- How confident are you that your scheduler works correctly?

- What edge cases would you test next if you had more time?

---

## 5. Reflection
**a. What went well**
- What part of this project are you most satisfied with?


**b. What you would improve**
- If you had another iteration, what would you improve or redesign?


**c. Key takeaway**
- What is one important thing you learned about designing systems or working with AI on this project?
