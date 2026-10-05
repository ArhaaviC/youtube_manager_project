import json

def load_data():
    try:
        with open('youtube.json','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.json','w') as file:
        json.dump(videos,file)

def list_all_videos(videos):
    if not videos:
        print("no videos yet")
        return
    print("----------------------")
    for index,video in enumerate(videos,start=1):
        print(f"{index}.{video['name']}, Duration: {video['time']}")
        print("-------------------")

def add_video(videos):
    name=input("enter video name")
    time=input("enter time")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    if not videos:
        return
    try:
        index=int(input("enter the video number to update: "))
    except ValueError:
        print("Please enter a number.")
        return
    if 1<= index <= len(videos):
        name=input("enter the new video name:  ")
        time=input("enter the new video time:  ")
        videos[index -1]= {'name':name,'time':time}
        save_data_helper(videos)
        print("Video Updated")
    else:
        print("Invalid video number.")

def delete_video(videos):
        list_all_videos(videos)
        if not videos:
            return
        try:
            index=int(input("enter the video  number to delete: "))
        except ValueError:
            print("please enter a number.")
            return
        if 1<= index <= len(videos):
            name=videos[index - 1]['name']
            confirm=input(f"Delete '{name}'? (y/n):  ").strip().lower()
            if confirm not in ('y','yes'):
                print("Cancelled")
                return
            del videos[index-1]
            save_data_helper(videos)
            print("video deleted")
        else:
            print("invalid video number")


def main():
    videos=load_data()

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
                list_all_videos(videos)
            case'2':
                add_video(videos)
            case'3':
                update_video(videos)
            case'4':
                delete_video(videos)
            case'5':
                break
            case _:
                print("Invalid choice")

if __name__ == "__main__":
    main()