import streamlit as st
import pandas as pd
import warnings
import streamlit_elements as elements
from streamlit_elements import elements, mui, html
warnings.filterwarnings('ignore')

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

st.title("화이팅 홈페이지")

with elements("multiple_children"):

    mui.Button(
        mui.icon.EmojiPeople,
        mui.icon.DoubleArrow,
        "Button with multiple children"
    )

    with mui.Button:
        mui.icon.EmojiPeople()
        mui.icon.DoubleArrow()
        mui.Typography("Button with multiple children")


with elements("style_mui_sx"):


    mui.Box(
        "Some text in a styled box",
        sx={
            "bgcolor": "background.paper",
            "boxShadow": 1,
            "borderRadius": 2,
            "p": 2,
            "minWidth": 300,
        }
    )



with elements("dashboard"):

    # 드래그 가능하고 크기를 조정할 수 있는 대시보드를 만들 수 있는 방법은 다음과 같습니다
    # Streamlit Elements에서 사용할 수 있는 모든 요소.

    from streamlit_elements import dashboard

    # 먼저 대시보드에 포함할 모든 요소에 대한 기본 레이아웃을 만듭니다

    layout = [
        # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
        # 매개변수: 요소_identifier, x_pos, y_pos, 너비, 높이, [항목 속성...]
        dashboard.Item("first_item", 0, 0, 2, 2),
        dashboard.Item("second_item", 2, 0, 2, 2, isDraggable=False, moved=False),
        dashboard.Item("third_item", 0, 2, 1, 1, isResizable=False),
    ]

    # 다음으로 'with' 구문을 사용하여 대시보드 레이아웃을 만듭니다. 레이아웃이 필요합니다
    # 첫 번째 매개변수로, 아래 GitHub 링크에서 추가 속성을 찾을 수 있습니다.

    with dashboard.Grid(layout):
        mui.Paper("First item", key="first_item")
        mui.Paper("Second item (cannot drag)", key="second_item")
        mui.Paper("Third item (cannot resize)", key="third_item")

    # 사용자가 대시보드 항목을 이동하거나 크기를 조정할 때 업데이트된 레이아웃 값을 검색하려면,
    # onLayoutChange 이벤트 파라미터에 콜백을 전달할 수 있습니다.

    def handle_layout_change(updated_layout):
        # You can save the layout in a file, or do anything you want with it.
        # You can pass it back to dashboard.Grid() if you want to restore a saved layout.
        print(updated_layout)

    with dashboard.Grid(layout, onLayoutChange=handle_layout_change):
        mui.Paper("First item", key="first_item")
        mui.Paper("Second item (cannot drag)", key="second_item")
        mui.Paper("Third item (cannot resize)", key="third_item")
        
        
with elements("nivo_charts"):
    import { ResponsiveBar } from '@nivo/bar'
    
    DATA = [
        {
            "country": "AD",
            "hot dog": 78,
            "hot dogColor": "hsl(360, 70%, 50%)",
            "burger": 107,
            "burgerColor": "hsl(279, 70%, 50%)",
            "sandwich": 130,
            "sandwichColor": "hsl(148, 70%, 50%)",
            "kebab": 39,
            "kebabColor": "hsl(4, 70%, 50%)",
            "fries": 148,
            "friesColor": "hsl(313, 70%, 50%)",
            "donut": 185,
            "donutColor": "hsl(315, 70%, 50%)"
        },
        {
            "country": "AE",
            "hot dog": 97,
            "hot dogColor": "hsl(109, 70%, 50%)",
            "burger": 128,
            "burgerColor": "hsl(299, 70%, 50%)",
            "sandwich": 170,
            "sandwichColor": "hsl(210, 70%, 50%)",
            "kebab": 27,
            "kebabColor": "hsl(1, 70%, 50%)",
            "fries": 8,
            "friesColor": "hsl(264, 70%, 50%)",
            "donut": 48,
            "donutColor": "hsl(342, 70%, 50%)"
        },
        {
            "country": "AF",
            "hot dog": 29,
            "hot dogColor": "hsl(188, 70%, 50%)",
            "burger": 96,
            "burgerColor": "hsl(182, 70%, 50%)",
            "sandwich": 10,
            "sandwichColor": "hsl(314, 70%, 50%)",
            "kebab": 119,
            "kebabColor": "hsl(12, 70%, 50%)",
            "fries": 154,
            "friesColor": "hsl(65, 70%, 50%)",
            "donut": 77,
            "donutColor": "hsl(285, 70%, 50%)"
        },
        {
            "country": "AG",
            "hot dog": 152,
            "hot dogColor": "hsl(315, 70%, 50%)",
            "burger": 79,
            "burgerColor": "hsl(104, 70%, 50%)",
            "sandwich": 124,
            "sandwichColor": "hsl(200, 70%, 50%)",
            "kebab": 107,
            "kebabColor": "hsl(75, 70%, 50%)",
            "fries": 192,
            "friesColor": "hsl(290, 70%, 50%)",
            "donut": 77,
            "donutColor": "hsl(349, 70%, 50%)"
        },
        {
            "country": "AI",
            "hot dog": 91,
            "hot dogColor": "hsl(141, 70%, 50%)",
            "burger": 134,
            "burgerColor": "hsl(110, 70%, 50%)",
            "sandwich": 175,
            "sandwichColor": "hsl(65, 70%, 50%)",
            "kebab": 72,
            "kebabColor": "hsl(117, 70%, 50%)",
            "fries": 90,
            "friesColor": "hsl(354, 70%, 50%)",
            "donut": 29,
            "donutColor": "hsl(290, 70%, 50%)"
        },
        {
            "country": "AL",
            "hot dog": 158,
            "hot dogColor": "hsl(301, 70%, 50%)",
            "burger": 89,
            "burgerColor": "hsl(353, 70%, 50%)",
            "sandwich": 81,
            "sandwichColor": "hsl(156, 70%, 50%)",
            "kebab": 32,
            "kebabColor": "hsl(64, 70%, 50%)",
            "fries": 35,
            "friesColor": "hsl(44, 70%, 50%)",
            "donut": 80,
            "donutColor": "hsl(78, 70%, 50%)"
        },
        {
            "country": "AM",
            "hot dog": 123,
            "hot dogColor": "hsl(138, 70%, 50%)",
            "burger": 73,
            "burgerColor": "hsl(140, 70%, 50%)",
            "sandwich": 139,
            "sandwichColor": "hsl(273, 70%, 50%)",
            "kebab": 171,
            "kebabColor": "hsl(119, 70%, 50%)",
            "fries": 176,
            "friesColor": "hsl(285, 70%, 50%)",
            "donut": 97,
            "donutColor": "hsl(353, 70%, 50%)"
        }
    ]

    const MyResponsiveBar = ({ data /* see data tab */ }) => (
        <ResponsiveBar
            data={data}
            keys={[
                'hot dog',
                'burger',
                'sandwich',
                'kebab',
                'fries',
                'donut'
            ]}
            indexBy="country"
            margin={{ top: 50, right: 130, bottom: 50, left: 60 }}
            padding={0.3}
            groupMode="grouped"
            valueScale={{ type: 'linear' }}
            indexScale={{ type: 'band', round: true }}
            colors={{ scheme: 'nivo' }}
            defs={[
                {
                    id: 'dots',
                    type: 'patternDots',
                    background: 'inherit',
                    color: '#38bcb2',
                    size: 4,
                    padding: 1,
                    stagger: true
                },
                {
                    id: 'lines',
                    type: 'patternLines',
                    background: 'inherit',
                    color: '#eed312',
                    rotation: -45,
                    lineWidth: 6,
                    spacing: 10
                }
            ]}
            fill={[
                {
                    match: {
                        id: 'fries'
                    },
                    id: 'dots'
                },
                {
                    match: {
                        id: 'sandwich'
                    },
                    id: 'lines'
                }
            ]}
            borderColor={{
                from: 'color',
                modifiers: [
                    [
                        'darker',
                        1.6
                    ]
                ]
            }}
            axisTop={null}
            axisRight={null}
            axisBottom={{
                tickSize: 5,
                tickPadding: 5,
                tickRotation: 0,
                legend: 'country',
                legendPosition: 'middle',
                legendOffset: 32,
                truncateTickAt: 0
            }}
            axisLeft={{
                tickSize: 5,
                tickPadding: 5,
                tickRotation: 0,
                legend: 'food',
                legendPosition: 'middle',
                legendOffset: -40,
                truncateTickAt: 0
            }}
            labelSkipWidth={12}
            labelSkipHeight={12}
            labelTextColor={{
                from: 'color',
                modifiers: [
                    [
                        'darker',
                        1.6
                    ]
                ]
            }}
            legends={[
                {
                    dataFrom: 'keys',
                    anchor: 'bottom-right',
                    direction: 'column',
                    justify: false,
                    translateX: 120,
                    translateY: 0,
                    itemsSpacing: 2,
                    itemWidth: 100,
                    itemHeight: 20,
                    itemDirection: 'left-to-right',
                    itemOpacity: 0.85,
                    symbolSize: 20,
                    effects: [
                        {
                            on: 'hover',
                            style: {
                                itemOpacity: 1
                            }
                        }
                    ]
                }
            ]}
            role="application"
            ariaLabel="Nivo bar chart demo"
            barAriaLabel={e=>e.id+": "+e.formattedValue+" in country: "+e.indexValue}
        />
    )
        


