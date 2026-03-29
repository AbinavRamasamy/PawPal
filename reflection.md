# PawPal+ Project Reflection

## 1. System Design
**a. Initial design**
- Briefly describe your initial UML design.
My initial UML design maps out the four core components required for PawPal+: Owner, Pet, Task, and Scheduler. It shows a clear hierarchy where an Owner is linked to their Pet, while the central Scheduler gathers those pets and their specific Tasks to generate an organized daily plan.

- What classes did you include, and what responsibilities did you assign to each?
I included Owner (to store user details and link to their pets), Pet (to hold specific animal data like species and name), and Task (to track care activities, durations, and priorities). Finally, the Scheduler class acts as the system's brain, responsible for collecting the tasks and executing the logic to organize them into a final schedule.


**b. Design changes**
- Did your design change during implementation?
My design did not change during implementation, as all of the classes in pawpal_system.py has the inital attributes and methods I intended them to have.

- If yes, describe at least one change and why you made it.
N/A
---

## 2. Scheduling Logic and Tradeoffs
**a. Constraints and priorities**
- What constraints does your scheduler consider (for example: time, priority, preferences)?
My scheduler considers priority (high/medium/low), scheduled start time (HH:MM), task duration, a daily time budget, and recurrence (daily/weekly). It also detects time conflicts when two tasks' windows overlap.

- How did you decide which constraints mattered most?
I decided that priority mattered most because a pet owner with limited time needs to know which tasks are non-negotiable (e.g., feeding, medication) before optional ones (e.g., grooming). Time budget came second because it shows overcommitment before the day starts, giving the owner a chance to reschedule rather than discover the problem mid-day.

**b. Tradeoffs**
- Describe one tradeoff your scheduler makes.
One tradeoff my scheduler makes is that it sorts by priority but does not automatically resolve time conflicts — it warns about them but gives no way to truly reorganize them. To overcome any time conflict, the user needs to mark a task as complete and remake the task and change the time slot.

- Why is that tradeoff reasonable for this scenario?
This tradeoff is reasonable because automatically rescheduling tasks would require knowing the owner's availability and preferences, which the system does not have. A warning gives the owner full control over how to resolve the conflict rather than silently moving tasks they may have intentionally placed at a specific time.
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
