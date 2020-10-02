from LinkedList import Node, arr_titles, LinkedList, arr_artist, arr_node_instance


def init_song_title(list_instance):
    # create an instance of array of Nodes with size of 5
    song_title = arr_titles

    # add all nodes to array
    for i in range(len(song_title)):
        song_title[i] = arr_titles[i]

    for i in range(0, 4):
        song_title[i].set_next_node(song_title[i + 1])

    list_instance.head = song_title[0]
    return list_instance


def init_artist_name(list_instance):
    artist_arr = arr_node_instance

    # iterate an array ranging from 5 and insert node child.
    for i in range(len(artist_arr)):
        artist_arr[i] = Node(arr_artist[i])

    for i in range(0, 4):
        artist_arr[i].set_next_node(artist_arr[i + 1])

    list_instance.head = artist_arr[0]
    return list_instance


def combine_two_list(linked_list_instance):
    two_list = arr_node_instance

    song_list_object = init_song_title(linked_list_instance).get_child_node()
    artist_list_object = init_artist_name(linked_list_instance).get_child_node()

    increment = 0
    while song_list_object and artist_list_object:
        two_list[increment] = Node(
            song_list_object.data + " - " + artist_list_object.data
        )
        song_list_object = song_list_object.next
        artist_list_object = artist_list_object.next
        increment += 1

    for i in range(0, 4):
        two_list[i].set_next_node(two_list[i + 1])

    linked_list_instance.head = two_list[0]

    linked_list_instance.traverse_list()


if __name__ == '__main__':
    # create list objects
    combine_two_list(LinkedList())
