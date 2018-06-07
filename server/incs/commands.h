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
#include "server.h"

typedef struct server_s server_t;
typedef struct client_s client_t;

typedef struct	command_s
{
	char	*name;
	void	(*ptrFnct)(server_t *, client_t *, char *);
}		command_t;

command_t	**init_commands(void);
command_t	*append_command(char *name, void (*ptrFnct)(server_t *, client_t *, char *));
void	map_size(server_t *server, client_t *client, char *str);
void	names_team(server_t *server, client_t *client, char *str);
void	map_content(server_t *server, client_t *client, char *str);
void	tile_content(server_t *server, client_t *client, char *str);
#endif /* !COMMANDS_H_ */
