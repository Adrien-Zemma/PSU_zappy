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
#include "map.h"

#define OK 0
#define BAD_PARAM 1
#define KO 2

typedef struct server_s server_t;
typedef struct client_s client_t;
typedef struct tile tile_t;

typedef struct	command_s
{
	double	time;
	char	*name;
	int	(*ptrFnct)(server_t *, client_t *, char *);
}		command_t;

command_t	**init_commands(t_parse *parse);
command_t	*append_command(char *name, int (*ptrFnct)(server_t *, client_t *, char *), double time);
int		map_size(server_t *server, client_t *client, char *str);
int		names_team(server_t *server, client_t *client, char *str);
int		map_content(server_t *server, client_t *client, char *str);
int		tile_content(server_t *server, client_t *client, char *str);
void		draw_tile(tile_t ***map, int fd, int i, int j);
int	player_level(server_t *server, client_t *client, char *str);
int	player_inventory(server_t *server, client_t *client, char *str);
int	player_position(server_t *server, client_t *client, char *str);
int	forward(server_t *server, client_t *client, char *str);
int	right(server_t *server, client_t *client, char *str);
int	left(server_t *server, client_t *client, char *str);
int	inventory(server_t *server, client_t *client, char *str);
int	look(server_t *server, client_t *client, char *str);
int	broadcast(server_t *server, client_t *client, char *str);
int	take_object(server_t *server, client_t *client, char *str);

#endif /* !COMMANDS_H_ */
