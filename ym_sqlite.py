import sqlite3

conn = sqlite3.connect('videos.db')
cursor_videos = conn.cursor()

table_create ="""
    CREATE TABLE IF NOT EXISTS VIDEOS(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    
    ); 

"""
cursor_videos.execute(table_create)
conn.commit()

def list_all_videos():
    cursor_videos.execute("SELECT * FROM VIDEOS")
    output = cursor_videos.fetchall()
    if not output:
        print("No videos yet")
        return
    for row in output:
        print(row)

def add_video():
    name = input("Enter video name:   ")
    time = input("Enter duration:     ")
    cursor_videos.execute("INSERT INTO VIDEOS (name,time) VALUES(?,?)", (name,time))
    conn.commit()

def update_video():
    id = input("enter id to update:   ")
    name = input("enter name of the video to update:   ")
    time = input("enter time to update:    ")
    cursor_videos.execute("UPDATE VIDEOS SET name = ?,time =? WHERE id = ?", (name,time,id) )
    conn.commit()
    if cursor_videos.rowcount == 0:
        print("No videos with that id")
    else:
        print("video updated")


def delete_video():
    id = input("enter id to update:   ")
    cursor_videos.execute("DELETE FROM VIDEOS WHERE id = ?", (id,) )
    conn.commit()    
    if cursor_videos.rowcount == 0:
        print("No videos with that id")
    else:
        print("video deleted")

        
def main():
    while True:
        print("\n********************Youtube Manager***********************")
        print("\n select an option")
        print("1.List all yb videos.")
        print("2.add a yb video.")
        print("3.Update a yb video details")
        print("4.delete a yb video")
        print("5.exit")

        choice=input("Enter your choice:  ")

        match choice:
            case'1':
                list_all_videos()
            case'2':
                add_video()
            case'3':
                update_video()
            case'4':
                delete_video()
            case'5':
                break
            case _:
                print("Invalid choice")

    conn.close()

if __name__ == "__main__":
    main()
