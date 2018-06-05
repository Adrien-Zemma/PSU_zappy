/*
** EPITECH PROJECT, 2018
** Zappy
** File description:
** Utils C file
*/

#include "parse.h"

const char commands_name[][64] = {
	"-p",
	"-x",
	"-y",
	"-n",
	"-c",
	"-f"
};

int	check_arg(char *command)
{
	for (int i = 0; i < 6; i++)
		if (strcmp(commands_name[i], command) == 0)
			return (i);
	return (-1);
}


void	free_tab(char **args)
{
	for (int i = 0; args[i]; i++) {
		free(args[i]);
		args[i] = NULL;
	}
	free(args);
	args = NULL;
}