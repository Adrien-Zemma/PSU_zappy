/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

static int	set_teams(server_t *server)
{
	size_t	size = 0;
	team_t	*team;

	for (; server->parse->teams[size]; size++);
	server->teams = malloc(sizeof(team_t) * size);
	if (!server->teams)
		return (84);
	for (size_t i = 0; i < size; i++) {
		team = &server->teams[i];
		team->name = server->parse->teams[i];
		team->absolute_max_players = server->parse->max_client;
		team->max_players = server->parse->max_client;
		team->current_players = 0;
	}
	return (0);
}

team_t	*find_team(server_t *server, char *name)
{
	size_t	size = 0;

	for (; server->parse->teams[size]; size++);
	for (size_t i = 0; i < size; i++) {
		if (!strcmp(server->teams[i].name, name)) {
			return (&server->teams[i]);
		}
	}
	return (NULL);
}

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
	if (set_teams(server) == 84)
		return (84);
	if (start_server(parse, server) == 84) {
		free_server(server);
		return (84);
	}
	return (0);
}
