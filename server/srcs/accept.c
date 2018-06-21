/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

int	set_client(server_t *server, char *str)
{
	client_t *client = server->clients[server->nb_client - 1];
	client->team = strdup(str);
	client->food = 1;
	client->linemate = 0;
	client->demaumere = 0;
	client->sibur = 0;
	client->mendiane = 0;
	client->phiras = 0;
	client->thystame = 0;
	client->level = 1;
	client->is_incanting = 0;
	client->id = server->nb_client;
	client->posX = ADD_MINERAL(0, server->parse->width);
	client->posY = ADD_MINERAL(0, server->parse->height);
	client->orientation = ADD_MINERAL(1, 5);
	client->command = queue_init();
	if (!client->command)
		return (84);
	append_player(&server->map[server->clients[server->nb_client - 1]->posY][server->clients[server->nb_client - 1]->posX],
		server->clients[server->nb_client - 1]);
	return (0);
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
	server->fds = realloc(server->fds, sizeof(int) * (server->nb_fd + 1));
	server->fds[server->nb_fd] = tmp;
	server->nb_fd++;
	server->nb_client++;
	server->clients = realloc(server->clients,
		sizeof(client_t *) * (1 + server->nb_client));
	server->clients[server->nb_client - 1] = malloc(sizeof(client_t));
	server->clients[server->nb_client] = NULL;
	server->clients[server->nb_client - 1]->fd = tmp;
	dprintf(tmp, "%d\n", server->nb_client);
	dprintf(tmp, "%d %d\n", server->parse->width, server->parse->height);
	tmp = set_client(server, str);
	send_connection(server->clients, server->clients[server->nb_client - 1]);
	return (tmp);
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
	if (!str)
		return (0);
	if (strcmp(str, "GRAPHIC") == 0)
		return (set_graphic(server, tmp));
	for (int i = 0; server->parse->teams[i] != NULL; i++)
		if (strncmp(server->parse->teams[i], str, strlen(server->parse->teams[i])) == 0)
			return (alloc_client(server, tmp, str));
	dprintf(tmp, "ko\n");
	return (0);
}
