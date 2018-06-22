##
## EPITECH PROJECT, 2018
## Project Name
## File description:
## zappy
##

NAME	= zappy_server

CC	= gcc

RM	= rm -f

SRCS	= ./server/srcs/accept.c \
	  ./server/srcs/commands/broadcast.c \
	  ./server/srcs/commands/connection.c \
	  ./server/srcs/commands/get_player_pos.c \
	  ./server/srcs/commands/gnp.c \
	  ./server/srcs/commands/incantation.c \
	  ./server/srcs/commands/inventory.c \
	  ./server/srcs/commands/look.c \
	  ./server/srcs/commands/look_east.c \
	  ./server/srcs/commands/look_south.c \
	  ./server/srcs/commands/look_west.c \
	  ./server/srcs/commands/map_content.c \
	  ./server/srcs/commands/map_size.c \
	  ./server/srcs/manage_tile.c \
	  ./server/srcs/commands/nb_connect.c \
	  ./server/srcs/commands/player_inventory.c \
	  ./server/srcs/commands/player_level.c \
	  ./server/srcs/commands/player_position.c \
	  ./server/srcs/commands/rotate_player.c \
	  ./server/srcs/commands/set_object.c \
	  ./server/srcs/commands/take_object.c \
	  ./server/srcs/commands/teams_name.c \
	  ./server/srcs/commands/tile_content.c \
	  ./server/srcs/commands.c \
	  ./server/srcs/getnextline.c \
	  ./server/srcs/main.c \
	  ./server/srcs/map.c \
	  ./server/srcs/parse.c \
	  ./server/srcs/queue.c \
	  ./server/srcs/read_command.c \
	  ./server/srcs/server.c \
	  ./server/srcs/set_socket.c \
	  ./server/srcs/timeout.c \
	  ./server/srcs/utils.c \
	  ./server/srcs/set_struct.c

OBJS	= $(SRCS:.c=.o)

CFLAGS = -I ./server/incs/
CFLAGS += -W -Wall -Wextra -g3

all: $(NAME)

$(NAME): $(OBJS)
	 $(CC) $(OBJS) -o $(NAME) $(LDFLAGS) -lm

clean:
	$(RM) $(OBJS)

fclean: clean
	$(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean re
