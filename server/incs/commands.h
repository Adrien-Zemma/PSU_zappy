/*
** EPITECH PROJECT, 2018
** Zappy
** File description:
** Commands H file
*/

#ifndef COMMANDS_H_
	#define COMMANDS_H_

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct	command_s
{
	char	*name;
	void	(*ptrFnct)(void *, void *, char *);
}		command_t;

command_t	**init_commands();
command_t	*append_command(char *name, void (*ptrFnct)(void *, void *, char *));

#endif /* !COMMANDS_H_ */
