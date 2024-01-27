
PID (Process ID):
A PID, or Process ID, is a unique numerical identifier assigned to each running process in a computer system. It is used by the operating system kernel to keep track of processes. PIDs are crucial for managing and interacting with processes, as they provide a way to refer to specific processes.

Process:
A process is an independent program or task that is executing in a computer system. It has its own memory space, resources, and state. Each process runs independently of other processes, and the operating system manages and schedules these processes for execution.

Finding a Process' PID:
To find a process's PID, you can use commands like ps (process status) or pgrep (process grep) in the terminal. For example:

bash
Copy code
ps aux | grep "process_name"
This will display information about the process, including its PID.

Killing a Process:
To terminate or kill a process, you can use the kill command followed by the process's PID. For example:

bash
Copy code
kill PID
You can also use the pkill command to kill a process by its name:

bash
Copy code
pkill "process_name"
Signal:
A signal is a software interrupt delivered to a process. It is a way for processes to communicate with each other or to instruct a process to perform a certain action. Signals can be used for various purposes, such as terminating a process, pausing a process, or instructing a process to reload its configuration.

Two Signals That Cannot Be Ignored:

SIGKILL (Signal 9): This signal immediately terminates a process and cannot be caught or ignored by the process. It is often used when a process needs to be forcefully terminated.

SIGSTOP (Signal 19): This signal causes a process to pause its execution temporarily. Like SIGKILL, it cannot be caught or ignored. The process remains in a suspended state until it receives a SIGCONT signal, which resumes its execution.

These signals are powerful and can be used carefully to manage and control processes in a system.






