#pragma once
class aobaddress{
	private:
	void* address;
	public:
		void* GetAddress() { return address; };
};

class WorldChrMan : aobaddress {
public:
	WorldChrMan();
	bool validateAobUsage();
	bool loadMainAobs();
	int getHP();
	int setHP(int value);

};
