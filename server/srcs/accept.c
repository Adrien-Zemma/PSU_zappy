/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

int	set_client(server_t *server, char *str)
{
	server->clients[server->nb_client - 1]->team = strdup(str);
	server->clients[server->nb_client - 1]->food = 1;
	server->clients[server->nb_client - 1]->linemate = 0;
	server->clients[server->nb_client - 1]->demaumere = 0;
	server->clients[server->nb_client - 1]->sibur = 0;
	server->clients[server->nb_client - 1]->mendiane = 0;
	server->clients[server->nb_client - 1]->phiras = 0;
	server->clients[server->nb_client - 1]->thystame = 0;
	server->clients[server->nb_client - 1]->level = 1;
	server->clients[server->nb_client - 1]->id = server->nb_client;
	server->clients[server->nb_client - 1]->posX = ADD_MINERAL(0, server->parse->width);
	server->clients[server->nb_client - 1]->posY = ADD_MINERAL(0, server->parse->height);
	server->clients[server->nb_client - 1]->orientation = ADD_MINERAL(1, 5);
	return (0);
}

void	print_graph_infos(server_t *server, client_t *client)
{
	map_size(server, client, NULL);
	map_content(server, client, NULL);
	names_team(server, client, NULL);
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
	if (strcmp(str, "GRAPHIC") == 0) {
		printf("add graphique client\n");
		server->fds[server->nb_fd] = tmp;
		server->nb_fd++;
		server->fds = realloc(server->fds, sizeof(int) * (server->nb_fd + 1));
		server->nb_client++;
		server->clients = realloc(server->clients,
			sizeof(client_t *) * (1 + server->nb_client));
		server->clients[server->nb_client - 1] = malloc(sizeof(client_t));
		server->clients[server->nb_client] = NULL;
		server->clients[server->nb_client - 1]->fd = tmp;
		print_graph_infos(server, server->clients[server->nb_client - 1]);
		dprintf(tmp, "%d %d\n", server->parse->width, server->parse->height);
		return (0);
	}
	for (int i = 0; server->parse->teams[i] != NULL; i++){
		if (strcmp(server->parse->teams[i], str) == 0){
			server->fds[server->nb_fd] = tmp;
			server->nb_fd++;
			server->fds = realloc(server->fds, sizeof(int) * (server->nb_fd + 1));
			server->nb_client++;
			server->clients = realloc(server->clients,
				sizeof(client_t *) * (1 + server->nb_client));
			server->clients[server->nb_client - 1] = malloc(sizeof(client_t));
			server->clients[server->nb_client] = NULL;
			server->clients[server->nb_client - 1]->fd = tmp;
			dprintf(tmp, "%d\n", server->nb_client);
			dprintf(tmp, "%d %d\n", server->parse->width, server->parse->height);
			return (set_client(server, str));
		}
	}
	dprintf(tmp, "ko\n");
	return (0);
}
