<html>
    <head>
        <title>CIS 322 REST-api demo: Laptop list</title>
    </head>    <body>


        <h1>List All Times</h1>
        <ul>
            <?php
            $json = file_get_contents('http://laptop-service/listAll');
            $obj = json_decode($json);
	          $laptops = $obj->result;
            foreach ($laptops as $l) {
                echo "<li>$l</li>";
            } 
            ?>
        </ul>

        <h1>List Open Times Only</h1>
        <ul>
            <?php
            $json2 = file_get_contents('http://laptop-service/listOpenOnly');
            $obj2 = json_decode($json2);
              $laptops2 = $obj2->result;
            foreach ($laptops2 as $l2) {
                echo "<li>$l2</li>";
            }
            
            ?>
        </ul>

        <h1>List Close Times Only</h1>
        <ul>
            <?php
            $json3 = file_get_contents('http://laptop-service/listCloseOnly');
            $obj3 = json_decode($json3);
              $laptops3 = $obj3->result;
            foreach ($laptops3 as $l3) {
                echo "<li>$l3</li>";
            }
            
            ?>
        </ul>

        <h1>List All Times With Json</h1>
        <ul>
            <?php
            $json = file_get_contents('http://laptop-service/listAll/json');
            $obj = json_decode($json);
              $laptops = $obj->result;
            foreach ($laptops as $l) {
                echo "<li>$l</li>";
            }
            
            ?>
        </ul>

        <h1>List Open Times Only With Json</h1>
        <ul>
            <?php
            $json2 = file_get_contents('http://laptop-service/listOpenOnly/json');
            $obj2 = json_decode($json2);
              $laptops2 = $obj2->result;
            foreach ($laptops2 as $l2) {
                echo "<li>$l2</li>";
            }
            
            ?>
        </ul>

        <h1>List Close Times Only With Json</h1>
        <ul>
            <?php
            $json3 = file_get_contents('http://laptop-service/listCloseOnly/json');
            $obj3 = json_decode($json3);
              $laptops3 = $obj3->result;
            foreach ($laptops3 as $l3) {
                echo "<li>$l3</li>";
            }
            
            ?>
        </ul>

        <h1>List All Times With CSV</h1>
        <ul>
            <?php
            $csv1 = file_get_contents('http://laptop-service/listAll/csv');
            $csv1.=',';
            $leng = strlen($csv1);
            $string = "";
            for($i=0; $i<$leng; $i++){
                if($csv1[$i] == ","){
                    echo "<li>$string</li>";
                    $string = ""; 
                }
                elseif($csv1[$i] != '"'){
                    $string.=$csv1[$i];
                }
            }
            
            ?>
        </ul>

        <h1>List Open Times Only With CSV</h1>
        <ul>
            <?php
            $csv2 = file_get_contents('http://laptop-service/listOpenOnly/csv');
            $csv2.=',';
            $leng = strlen($csv2);
            $string = "";
            for($i=0; $i<$leng; $i++){
                if($csv2[$i] == ","){
                    echo "<li>$string</li>";
                    $string = ""; 
                }
                elseif($csv2[$i] != '"'){
                    $string.=$csv2[$i];
                }
            }
            
            
            ?>
        </ul>

        <h1>List Close Times Only With CSV</h1>
        <ul>
            <?php
            $csv3 = file_get_contents('http://laptop-service/listCloseOnly/csv');
            $csv3.=',';
            $leng = strlen($csv3);
            $string = "";
            for($i=0; $i<$leng; $i++){
                if($csv3[$i] == ","){
                    echo "<li>$string</li>";
                    $string = ""; 
                }
                elseif($csv3[$i] != '"'){
                    $string.=$csv3[$i];
                }
            }
            
            
            ?>
        </ul>

    </body>
</html>
