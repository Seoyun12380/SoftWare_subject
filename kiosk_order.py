# 주문 정보를 담는 클래스
class Order:
    def __init__(self, menu_item):
        self.menu_item = menu_item	# 사용자가 주문하는 메뉴의 이름
        self.is_paid = False		# 결제가 잘 되었는지 확인

# 결제를 담당하는 클래스
class Pay:
    def process_payment(self, order):
        print(f"[카드 리더기] '{order.menu_item}' 결제 요청 받았습니다...")
        order.is_paid = True		# 결제가 되었다면 아래를 출력
        print("[카드 리더기] 결제가 완료되었습니다.") 	
        return True

# 주방에서 주문을 받는 클래스
class Kitchen:
    def receive_order(self, order):
        print(f"[주방] '{order.menu_item}' 주문을 접수했습니다. 맛있게 만드는 중입니다!")

# 키오스크 전체 흐름을 제어하는 클래스
class Kiosk:
    def __init__(self):
        self.payment_terminal = Pay()
        self.kitchen = Kitchen()

    def take_order(self, menu_item):
        print(f"[키오스크] '{menu_item}' 메뉴를 선택하셨습니다!")
        order = Order(menu_item)		# 주문 객체 생성

        if self.payment_terminal.process_payment(order):
            self.kitchen.receive_order(order)	#결제에 성공하면 주방에 주문 전송
            print("[키오스크] 주문이 완료되었습니다. 대기번호는 15번입니다. 잠시만 기다려주세요 :)")
        else:
            print("[키오스크] 결제에 실패했습니다. 다시 시도해주세요.")


# 실행
if __name__ == "__main__":
    kiosk = Kiosk()
    kiosk.take_order("떡볶이")