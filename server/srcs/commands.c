/*
** EPITECH PROJECT, 2018
** Zappy
** File description:
** Commands C file
*/

#include "commands.h"

void	test(void *a, void *b, char *cc)
{
	(void)a;
	(void)b;
	(void)cc;
}

command_t	**init_commands()
{
	const int	i = 3;
	command_t	**node = malloc(sizeof(command_t *) * (i + 1));
	
	if (!node)
		return NULL;
	node[0] = append_command("MAP", test);
	node[1] = append_command("MAPz", test);
	node[2] = append_command("MAPE", test);
	node[i] = NULL;
	return node;

}

command_t	*append_command(char *name, void (*ptrFnct)(void *, void *, char *))
{
	command_t	*node = malloc(sizeof(command_t));

	if (!node)
		return NULL;
	node->name = name;
	node->ptrFnct = ptrFnct;
	return node;
}

void		parse_command(command_t **command, char *cmd)
{
	printf("Received [%s]\n", cmd);
	for (int i = 0; command[i]; i++)
		if (strncmp(command[i]->name, cmd, strlen(command[i]->name)) == 0)
			command[i]->ptrFnct(NULL, NULL, NULL);
}