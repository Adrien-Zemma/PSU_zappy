/*
** EPITECH PROJECT, 2018
** Zappy
** File description:
** Utils C file
*/

#include "parse.h"

const char	commands_name[][64] =
{
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

int	c_count(char *str, char c)
{
	int n = 0;

	for (int i = 0; str[i]; i++)
		if (str[i] == c)
			n++;
	return (n);
}

char	*parse_command(char *command, char c, int nb)
{
	int count = 0;
	int size = 2;
	char *new = malloc(sizeof(char) * size);

	if (c_count(command, c) < nb)
		return NULL;
	while (command && nb > count) {
		if (*command == c)
			count++;
		command++;
	}
	for (int i = 0; *command && *command != c; i++) {
		new[i] = *command;
		new = realloc(new, sizeof(char) * ++size);
		command++;
	}
	new[size - 2] = '\0';
	new[size - 1] = '\0';
	return (new);
}
