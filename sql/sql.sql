SELECT todos_song.name
FROM todos_songmembers
JOIN todos_song
ON todos_songmembers.song_id_id=todos_song.id
WHERE todos_songmembers.member_id_id = (
	SELECT id
	FROM todos_member
	WHERE name = "秋元真夏"
);

