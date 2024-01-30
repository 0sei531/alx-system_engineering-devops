#include <sys/types.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

/**
 * infinite_while - runs forever and returns nothing
 * Return: 0 in the end
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Creates 5 zombie processes.
 *
 * Description: For every zombie process created, it
 * displays Zombie process created, PID: ZOMBIE_PID
 *
 * Return: 0
 */
int main(void)
{
	pid_t zombie_pid;
	int zombie;
	int status;  /* To store the exit status of child processes */

	for (zombie = 0; zombie < 5; zombie++)
	{
		zombie_pid = fork();
		if (zombie_pid > 0)
		{
			printf("Parent: Created Zombie process, PID: %d\n", zombie_pid);
			waitpid(zombie_pid, &status, 0);  /* Reap the child process */
			printf("Parent: Zombie process, PID: %d exited with status: %d\n", zombie_pid, status);
		}
		else
		{
			printf("Child: Zombie process created, PID: %d\n", getpid());
			exit(zombie + 1);  /* Child exits with a status code */
		}
	}

	infinite_while();

	return (0);
}

