package com.zomnipotential.qualityapi;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.web.servlet.MockMvc;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@SpringBootTest
@AutoConfigureMockMvc
public class QualityApiApplicationTests {

    @Autowired
    private MockMvc mockMvc;

    @Test
    void testSummaryEndpointReturnsJson() throws Exception {
        mockMvc.perform(get("/v1/quality/summary"))
                .andExpect(status().isOk())
                .andExpect(content().contentType("application/json"))
                .andExpect(jsonPath("$[0].ticket_id").exists()); // Basic check that JSON looks correct
    }
}