# PawPal+ Project Reflection

## 1. System Design
**a. Initial design**
- Briefly describe your initial UML design.
My initial UML design maps out the four core components required for PawPal+: Owner, Pet, Task, and Scheduler. It shows a clear hierarchy where an Owner is linked to their Pet, while the central Scheduler gathers those pets and their specific Tasks to generate an organized daily plan.

- What classes did you include, and what responsibilities did you assign to each?
I included Owner (to store user details and link to their pets), Pet (to hold specific animal data like species and name), and Task (to track care activities, durations, and priorities). Finally, the Scheduler class acts as the system's brain, responsible for collecting the tasks and executing the logic to organize them into a final schedule.


**b. Design changes**
- Did your design change during implementation?
Yes. While the four core classes stayed the same, the UML needed to be updated to reflect new attributes and methods added during the build.

- If yes, describe at least one change and why you made it.
The most significant change was to the Task class — the original UML only had title, duration_minutes, and priority. During implementation, time, completed, recurrence, and mark_complete() were added to support scheduling by time slot, conflict detection, and recurring tasks. The Pet class also gained a tasks list and add_task() method once it became clear that pets needed to track their own tasks independently of the Scheduler.
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
I used AI primarily for debugging and refactoring. I described the behavior and asked the AI to help me trace through the overlap condition. I also used it during the UML design phase to think through which class should own certain classes, like the task: Pet or Scheduler? It helped understand the inner workings of the codebase.

- What kinds of prompts or questions were most helpful?
The most helpful prompts were specific and included context. Asking for explanations of why a suggestion worked, rather than just what to change, helped me actually understand the fix.


**b. Judgment and verification**
- Describe one moment where you did not accept an AI suggestion as-is.
When I asked for help implementing recurrence, the AI suggested storing recurring tasks as a list of pre-generated Task objects for every future date. I did not accept that approach because it would create unnecessary objects upfront and make the scheduler much harder to read and test

- How did you evaluate or verify what the AI suggested?
I traced through what the suggested approach would look like in practice — if a task recurred daily for a year, the system would generate 365 objects at creation time, which felt wrong for a simple scheduling tool. I instead kept recurrence as a string attribute on the Task and handled it at display time, which was simpler and matched the existing design.

---

## 4. Testing and Verification
**a. What you tested**
- What behaviors did you test?
I tested adding tasks to a pet and verifying they appeared in the generated schedule, the priority sort order (high before medium before low), conflict detection between overlapping time windows, the time budget warning when total task duration exceeded the daily limit, and marking a task as complete.

- Why were these tests important?
These tests covered the core promise of the scheduler — that it organizes tasks correctly and flags problems before the owner's day starts. If priority sorting or conflict detection were broken, the output would be misleading, which is worse than no schedule at all since the owner would trust incorrect information.


**b. Confidence**
- How confident are you that your scheduler works correctly?
I am pretty confident that my scheduler works correctly because it passes all of my tests. I know that it can do the basics, as they are solid, but I do not know the results if there were many edge cases.

- What edge cases would you test next if you had more time?
I would test a task with a duration of 0 minutes (which the UI blocks but the backend does not), starting a new day on the 7th day to verify weekly recurring tasks reset correctly, and adding a task with a malformed time value to see whether conflict detection raises an error or silently produces wrong results. I also don't know if actions that take up longer than the remaining day register correctly (60 minute action after 11:00 pm, before 12 AM).

---

## 5. Reflection
**a. What went well**
- What part of this project are you most satisfied with?
I am most satisfied with the robustness of the project, as it has a wide variety of options and new UI elements that makes the current version of the app much better than a simple working version. I like how the current project seems more complete than it may have been intended to be.

**b. What you would improve**
- If you had another iteration, what would you improve or redesign?
If I had another iteration, I would redesign the filtering option (currently a sidebar), and I would add additional functionality to make it easier to keep using. For example, a way to intuitively reorder events or edit the Tasks without having to delete and recreate it from scratch.

**c. Key takeaway**
- What is one important thing you learned about designing systems or working with AI on this project?
AI is most useful when you already have a clear picture of what you want; it accelerates execution but does not replace design thinking. On this project, the moments where AI help was most effective were when I could describe a specific, concrete problem. When I asked broad questions, the suggestions were generic and sometimes pointed in the wrong direction or kept asking questions about what to change.

