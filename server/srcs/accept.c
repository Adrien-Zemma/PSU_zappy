/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

int	set_client(server_t *server, char *str, client_t *client)
{
	client->food = 10;
	client->linemate = 0;
	client->demaumere = 0;
	client->sibur = 0;
	client->mendiane = 0;
	client->phiras = 0;
	client->thystame = 0;
	client->level = 1;
	client->is_incanting = 0;
	client->id = server->nb_client;
	client->pos_x = ADD_MINERAL(0, server->parse->width);
	client->pos_y = ADD_MINERAL(0, server->parse->height);
	client->orientation = ADD_MINERAL(1, 5);
	client->command = queue_init();
	client->time = 0;
	append_player(&server->map[client->pos_y][client->pos_x], client);
	client->team = find_team(server, str);
	free(str);
	return (client->fd);
}

void	print_graph_infos(server_t *server, client_t *client)
{
	map_size(server, client, NULL);
	dprintf(client->fd, "sgt %d\n", server->parse->freq);
	map_content(server, client, NULL);
	names_team(server, client, NULL);
}

int	set_graphic(server_t *server, int tmp)
{
	server->fds = realloc(server->fds, sizeof(int) * (server->nb_fd + 1));
	server->fds[server->nb_fd] = tmp;
	server->nb_fd++;
	server->nb_client++;
	server->clients = realloc(server->clients,
		sizeof(client_t *) * (1 + server->nb_client));
	server->clients[server->nb_client - 1] = malloc(sizeof(client_t));
	server->clients[server->nb_client] = NULL;
	server->clients[server->nb_client - 1]->fd = tmp;
	server->clients[server->nb_client - 1]->id = -1;
	server->clients[server->nb_client - 1]->command = queue_init();
	print_graph_infos(server, server->clients[server->nb_client - 1]);
	return (0);
}

int	alloc_client(server_t *server, int tmp, char *str)
{
	client_t	*client;

	server->fds = realloc(server->fds, sizeof(int) * (server->nb_fd + 1));
	server->fds[server->nb_fd] = tmp;
	server->nb_fd++;
	server->nb_client++;
	server->clients = realloc(server->clients,
		sizeof(client_t *) * (1 + server->nb_client));
	server->clients[server->nb_client - 1] = malloc(sizeof(client_t));
	server->clients[server->nb_client] = NULL;
	server->clients[server->nb_client - 1]->fd = tmp;
	client = server->clients[server->nb_client - 1];
	tmp = set_client(server, str, client);
	if (!client->team
	|| client->team->max_players - ++client->team->current_players < 0) {
		dprintf(client->fd, "ko\n");
		remove_client(server, client->fd);
		return (tmp);
	}
	return (write_map(tmp, client, server));
}

int	set_accept(server_t *server)
{
	int	tmp;
	struct	sockaddr_in	s_sin_client;
	socklen_t	s_sin_size = sizeof(s_sin_client);
	char	*str;

	tmp = accept(server->fd, (struct sockaddr *)&s_sin_client, &s_sin_size);
	if (tmp == -1)
		perror("accept :");
	dprintf(tmp, "WELCOME\n");
	str = getnextline(tmp);
	return (check_str_accept(tmp, str, server));
}
