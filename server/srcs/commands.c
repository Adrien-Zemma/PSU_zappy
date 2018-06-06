/*
** EPITECH PROJECT, 2018
** Zappy
** File description:
** Commands C file
*/

#include "commands.h"

command_t	**init_commands(void)
{
	const int	i = 3;
	command_t	**node = malloc(sizeof(command_t *) * (i + 1));
	
	if (!node)
		return NULL;
	node[0] = append_command("msz", map_size);
	node[1] = append_command("tna", names_team);
	node[2] = append_command("mct", map_content);
	node[i] = NULL;
	return node;
}

command_t	*append_command(char *name, void (*ptrFnct)(server_t *, client_t *, char *))
{
	command_t	*node = malloc(sizeof(command_t));
	
	if (!node)
		return NULL;
	node->name = name;
	node->ptrFnct = ptrFnct;
	return node;
}