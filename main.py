from controller import MainTasks
def main():
    while True:
        task = MainTasks.AllTask()
        choice = input("📝 Enter your choice: ").strip()
        if choice == '1':
            task.cleanup_menu()
        elif choice == '2':
            compress_menu()
        elif choice == '3':
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
