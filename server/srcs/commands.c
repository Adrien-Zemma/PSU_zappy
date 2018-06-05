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
	node[0] = append_command("MAP", test, 2);
	node[1] = append_command("MAPz", test, 2);
	node[2] = append_command("MAPE", test, 2);
	node[i] = NULL;
	return node;

}

command_t	*append_command(char *name, void (*ptrFnct)(void *, void *, char *), size_t max_args)
{
	command_t	*node = malloc(sizeof(command_t));

	if (!node)
		return NULL;
	node->name = name;
	node->ptrFnct = ptrFnct;
	node->max_args = max_args;
	return node;
}