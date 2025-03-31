hard_reasoning_template_de = '''Sie sind beauftragt, ein logisches Denkproblem basierend auf einer gegebenen Persona-Beschreibung zu erstellen. Das Problem sollte relevant für die Expertise und den beruflichen Kontext der Persona sein.

Hier ist die Persona-Beschreibung:

{persona}

Verwenden Sie diese Persona-Beschreibung, um ein logisches Denkproblem zu erstellen, das die folgenden Kriterien erfüllt:

1. Das Problem sollte direkt mit dem Fachgebiet oder Arbeitsumfeld der Persona zusammenhängen.
2. Es sollte ein Szenario beinhalten, das logisches Denken und Problemlösungsfähigkeiten erfordert.
3. Das Problem sollte mehrere Elemente oder Variablen enthalten, die berücksichtigt werden müssen.
4. Es sollten klare Einschränkungen oder Regeln vorhanden sein, die das Problem regeln.
5. Das Problem sollte eine eindeutige, logische Lösung haben, die durch sorgfältiges Überlegen erreicht werden kann.

Ihr logisches Denkproblem sollte aus den folgenden Komponenten bestehen:
1. Eine kurze Einführung, die das Szenario beschreibt
2. Eine klare Darstellung des zu lösenden Problems oder der zu beantwortenden Frage
3. Eine Liste relevanter Fakten, Einschränkungen oder Regeln
4. Die spezifische Frage oder Aufgabe, die beantwortet oder gelöst werden muss

Zielen Sie auf ein hohes Komplexitätsniveau ab - das Problem sollte herausfordernd sein, um sorgfältiges Nachdenken zu erfordern aber nur simple Mathematik erfordern (Addition, Substraktion, Multiplikation, Division).

Überlegen Sie zunächst, ob das Problem auch zu lösen ist und präsentieren Sie erst dann Ihr logisches Denkproblem. Beginnen Sie direkt mit der Beschreibung des Problems ohne Überschrift.

Denken Sie daran, einen professionellen Ton beizubehalten und eine Terminologie zu verwenden, die dem Fachgebiet der Persona angemessen ist.'''


hard_reasoning_template_en = '''You are tasked with generating a logical reasoning problem based on a given persona description. The problem should be relevant to the persona's expertise and professional context.

Here is the persona description:

{persona}

Using this persona description, create a logical reasoning problem that meets the following criteria:

1. The problem should be directly related to the persona's field of expertise or work environment.
2. It should involve a scenario that requires logical thinking and problem-solving skills.
3. The problem should include multiple elements or variables that need to be considered.
4. There should be clear constraints or rules that govern the problem.
5. The problem should have a definitive, logical solution that can be reached through careful reasoning.

Your logical reasoning problem should consist of the following components:
1. A brief introduction setting up the scenario
2. A clear statement of the problem or question to be solved
3. A list of relevant facts, constraints, or rules
4. The specific question or task that needs to be answered or completed

Aim for a high level of complexity - the problem should be challenging enough to require careful thought, while only involving basic arithmetic operations (addition, subtraction, multiplication, division).

First, consider whether the problem can be solved, and only then present your logical reasoning problem. Start directly with the description of the problem without a heading.

Remember to maintain a professional tone and use terminology appropriate to the persona's field of expertise.'''


system_de = '''Du bist ein Professor der Deduktion und ein genialer Schlussfolgerer, der dem Nutzer mit maximaler Genauigkeit antwortet. Um dies zu tun, wirst du zuerst darüber nachdenken, was der Nutzer fragt, und Schritt für Schritt überlegen.

Um das Problem zu lösen, sollten Überlegungen und Reflektionen genutzt werden. Die folgenden Schritte sollten dabei beachtet werden:

- Erfassen, was der Nutzer fragt und die in der Anfrage erwähnten Einschränkungen verstehen.
- Auflisten der vom Nutzer genannten Einschränkungen.
- Vorschlagen einer Lösung für die Frage des Nutzers unter Berücksichtigung aller Einschränkungen.
- Überprüfen, ob die Lösung mit den Einschränkungen übereinstimmt.
- Ausgeben der abschließenden Lösung.
Am Ende deiner Überlegungen musst du zu einem Schluss kommen und die Lösung präsentieren.'''


system_en = '''You are a professor of deduction and a brilliant reasoner that responds to the user with maximum accuracy. To do this, you will first think about what the user is asking and consider it step by step.

To solve the problem, considerations and reflections should be used. The following steps should be observed:

- Understand what the user is asking and comprehend the constraints mentioned in the request.
- List the constraints mentioned by the user.
- Propose a solution to the user's question, taking all constraints into account.
- Verify if the solution aligns with the constraints.
- Output the final solution.
At the end of your considerations, you must come to a conclusion and present the solution.'''