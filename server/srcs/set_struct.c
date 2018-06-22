/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

int	set_struct_server(server_t *server, t_parse *parse)
{
	server->clients = malloc(sizeof(client_t *) * 1);
	server->parse = parse;
	server->command = init_commands(parse);
	server->clients[0] = NULL;
	server->nb_client = 0;
	server->fds = malloc(sizeof(int) * 1);
	server->map = init_map(parse->width, parse->height);
	server->nb_fd = 0;
	if (set_socket(parse, server) == 84)
		return (84);
	if (start_server(parse, server) == 84) {
		free_server(server);
		return (84);
	}
	return (0);
}
